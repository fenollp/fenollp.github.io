---
published: true
title: 'MediaPipe tutorial: Find memes matching your facial expression 😮'
layout: post
categories: [mediapipe, powder.gg, memes, tensorflow, opencv, inference, ios]
permalink: mediapipe-memes-matching-your-facial-expression
---

*Originally [posted on Jun 5, 2020](https://powderapp.medium.com/mediapipe-tutorial-find-memes-that-match-your-facial-expression-9bf598da98c0) during a collaboration between Google and Powder.gg. Some links were updated.*

A post by Pierre Fenoll, Senior Lead Back-End Engineer at Powder.gg

## Introduction
[Powder.gg](https://powder.gg/) is a startup located in the beautiful [district of Marais](https://www.google.com/maps/place/Le+Marais,+Paris,+France/data=!4m2!3m1!1s0x47e66e03cdce4ae9:0x38cfa580446f9e46?sa=X&ved=2ahUKEwiUiamQ6InoAhUI2qwKHen0BH4Q8gEwHnoECBcQBA) in Paris. We are working hard to help gamers edit their highlights with machine learning on mobile. AI, memes, sound and visual effects make up the toolkit we aim to provide to people all around the world to help them understand each other better. Our team has been using MediaPipe extensively to create our machine learning enabled video editing app for gamers.We created this tutorial to show how you can use MediaPipe to create your next ML enabled app.

## Goals and requirements
Say you’re chatting on your phone with some friends. Your friend, Astrid wrote something amusing and you wanted to post a funny image related to hers . There’s this picture you really want to post but it’s not on your phone and now you’re just trying different words in your search engine of choice without any success. This image is so clear in your mind, the words to look it up just don’t come out right somehow. If only you could just make the same hilarious face to your phone and it would find it for you!

Say you’re chatting on your phone with some friends. Your friend, Astrid wrote something amusing and you wanted to post a funny image related to hers . There’s this picture you really want to post but it’s not on your phone and now you’re just trying different words in your search engine of choice without any success. This image is so clear in your mind, the words to look it up just don’t come out right somehow. If only you could just make the same hilarious face to your phone and it would find it for you!

Here’s the app we’re building.

<div style="padding:177.78% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/426179805?h=f9aaec4917&autoplay=1&loop=1&portrait=0" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

> Figure 1: Demo of the end result iOS app


## Machine Learning model for our pipeline
We need a machine learning model that can determine how similar 2 images with facial expressions are. The emotions/facial expression recognition module we use is based on [a 2019 paper](https://research.google/pubs/pub47657/) published by Raviteja Vemulapalli and Aseem Agarwala, from Google AI, titled A Compact Embedding for Facial Expression Similarity. At Powder, we re-implemented the approach described in that paper. We then improved on this approach by [using knowledge distillation](https://arxiv.org/abs/1503.02531), a technique whereby an often [smaller student network is trained to mimic the predictions made by a teacher network](https://medium.com/neuralmachine/knowledge-distillation-dc241d7c2322). We have found that using knowledge distillation leads to an even more accurate model. We also incorporated millions of additional unlabelled images in the knowledge distillation process, and found this improved performance even further.

Specifically, the original Google paper reported 81.8% “triplet prediction accuracy” of their model on their face triplets dataset. Our re-implementation of this approach yielded closer to 79% accuracy, with the drop likely being due to our not-quite-complete reproduction of their dataset (due to source images being removed from Flickr). Using knowledge distillation with additional unlabelled data, we were then able to improve this score to 85%.

Specifically, the original Google paper reported 81.8% “triplet prediction accuracy” of their model on their face triplets dataset. Our re-implementation of this approach yielded closer to 79% accuracy, with the drop likely being due to our not-quite-complete reproduction of their dataset (due to source images being removed from Flickr). Using knowledge distillation with additional unlabelled data, we were then able to improve this score to 85%.

<img align=center style="background-color:white" src="./assets/sha256/bf5ebf4d929fc8162273de38028e74375a91beb64836c6171e067b27e03cf1aa.png"/>

> Figure 2: Block diagram illustrating what model does images -> embedding


For a quick introduction into [MediaPipe](https://mediapipe.dev/)
* Hello World examples: [Android](https://google.github.io/mediapipe/getting_started/hello_world_android.html) [iOS](https://google.github.io/mediapipe/getting_started/hello_world_ios.html) [Python](https://google.github.io/mediapipe/getting_started/python_framework.html) [Javascript](https://google.github.io/mediapipe/getting_started/javascript.html) [C++](https://google.github.io/mediapipe/getting_started/hello_world_cpp.html)
* [Video from MediaPipe Seattle 2020 meet-up](https://www.youtube.com/watch?v=qXs0QZ6VWS8)

## Prototyping the pipeline on the desktop
In order to prototype the inference pipeline using MediaPipe that will find memes that have similar facial expressions from a video, we started out building the desktop prototype as iteration can be much faster than with a mobile in the loop. After the desktop prototype, we can optimize for our main target platform: Apple iPhones. We start by creating a C++ demonstration program similar to [the provided desktop examples](https://github.com/google/mediapipe/tree/master/mediapipe/examples/desktop) and build our graphs from there.


<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/383553724?h=42a57bb409&autoplay=1&loop=1&portrait=0" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

> Figure 3: Animated gif showing demo of the MediaPipe pipeline showing how we match facial expressions in a video to internet memes

Although it is possible to create a repository separate from MediaPipe ([as demonstrated here](https://github.com/mgyong/mediapipe_addons/tree/master/helloworld)), we prefer to develop our graphs and calculators in our own fork of the project. This way upgrading to the latest version of MediaPipe is just a git-rebase away.

To avoid potential conflicts with MediaPipe code we replicate the folder architecture under a subdirectory of mediapipe: graphs, calculators and the required BUILD files.

MediaPipe comes with many calculators that are documented, tested and sometimes optimized for multiple platforms so we try as much as possible to leverage them. When we really need to create new calculators we try to design them so that they can be reused in different graphs. For instance, we designed a calculator that displays its input stream to an OpenCV window and which closes on a key press. This way we can quickly plug into various parts of a pipeline and glance at the images streaming through.

## MediaPipe Graph — Face Detection followed by Face embedding
We construct a graph that finds faces in a video, takes the first detection then extracts a 64-dimensions vector describing that face. Finally it goes through a custom-made calculator that compares these embeddings against a large set of vector-images pairs and sorts the top 3 results using Euclidean distance.

<img align=center style="background-color:white" src="./assets/sha256/bc04e63ca1c1a69fea1b75f349c7a4f66fc57a9ece1144841e42735cf85d4a10.png"/>

> Figure 4: The algorithm behind FacialSearch

Face detection is performed with [MediaPipe’s own SSD based selfie face detector graph](https://google.github.io/mediapipe/solutions/face_detection). We turned the gist of it into a [subgraph](https://google.github.io/mediapipe/framework_concepts/graphs.html#subgraph) so our graph can easily link against it as well as some of our other graphs. Subgraphs are great for reusability and can be thought of as modules. We tend to create one per model just for the benefit of encapsulation.

Embeddings are extracted within the FaceEmbeddingsSubgraph using our Tensorflow Lite model and streamed out as a vector of 64 floats. This subgraph takes care of resizing the input image and converting to and from Tensorflow tensors.

Then our ClosestEmbeddingsCalculator expects this vector, computes the distance to each vector in the embedded database and streams out the top matches as Classifications, with the distance as score. The database is loaded as a side packet and can be generated with the help of a Shell script. A sample database of around 400 entries is provided.

<p align="middle">
  <img src="./assets/sha256/46657829e7cc252601130e570580a5db48c4f1a66280121ecab63f592f76d345.png" width="33%"/>
  <img src="./assets/sha256/b26b7f91b9e0767da0603a5ab3516093d8479cfbf6f72301ccf543e00f9185b3.png" width="33%"/>
  <img src="./assets/sha256/5d60b91e313b495f7b325299b2e22bf9e946c5dfbf90505ee0627a86899584b5.png" width="33%"/>
</p>


> Figure 5. Left to right, top down: ① main graph ② FaceDetection subgraph ③ FaceEmbeddings subgraph

## Issues we faced
You may have noticed in the above GPU FaceEmbeddingsSubgraph the use of the [GpuBufferToImageFrame](https://github.com/google/mediapipe/blob/710fb3de58dc10b7bc75f9cb758300c9016a5e4f/mediapipe/gpu/gpu_buffer_to_image_frame_calculator.cc) calculator. This moves an image from GPU to the host CPU. It turns out our model uses instructions that are not supported by the current version of the Tensorflow Lite GPU interpreter. Running it would always return the same values and output the following warnings when initializing the graph:

```
ERROR: Next operations are not supported by GPU delegate:
MAXIMUM: Operation is not supported.
MEAN: Operation is not supported.
First 0 operations will run on the GPU, and the remaining 81 on the CPU.
```

There are multiple ways to fix this:
* You can re-train your model such that the generated tflite file uses only supported operations.
* You can implement the operations in C++ and use MediaPipe’s [TfLiteCustomOpResolverCalculator](https://github.com/google/mediapipe/blob/710fb3de58dc10b7bc75f9cb758300c9016a5e4f/mediapipe/calculators/tflite/tflite_custom_op_resolver_calculator.cc) to provide them to the interpreter.
* If your model runs fine on CPU you can just make sure inference always runs on CPU by moving its inputs to CPU. Moving data from GPU to host CPU is however not free so inference should be a bit slower.

We opted for the simplest option for this tutorial as runtime costs appeared minimal. We may be providing a model that can run on GPU in the future.

## Running on the desktop
First make sure the images of our database are on your system. These come from [imgflip.com](https://imgflip.com/) and were selected on the criterion that they contain at least one human face. There are mostly pictures but some drawings as well. Download them with:

```sh
python mediapipe/examples/facial_search/images/download_images.py
```

Then you are free to re-generate the embeddings data. This process uses our graph on the images we downloaded to extract a float vector per image. These are then written to a C++ header file to constitute the database. Keep in mind that there can be some differences in floating point precision from one platform to another so you might want to generate the embeddings on the targeted platform. Run:

```sh
./mediapipe/examples/facial_search/generate_header.sh \
    mediapipe/examples/facial_search/images
```

Now run the demo on CPU [with](https://gist.github.com/fenollp/f2f7ab008d2f028fb59eeb4b11e87028#file-cpu-sh):
```sh
bazel run --platform_suffix=_cpu \
  --copt=-fdiagnostics-color=always --run_under="cd $PWD && " \
  -c opt --define MEDIAPIPE_DISABLE_GPU=1 \
  mediapipe/examples/facial_search/desktop:facial_search \
  -- \
  --calculator_graph_config_file=mediapipe/examples/facial_search/graphs/facial_search.pbtxt \
  --images_folder_path=mediapipe/examples/facial_search/images/
```

And run the demo on GPU [with](https://gist.github.com/fenollp/b873521d9f43c5d3ab7f1cf03732dd36#file-gpu-sh):
```sh
bazel run --platform_suffix=_gpu \
  --copt=-fdiagnostics-color=always --run_under="cd $PWD && " \
  -c opt --copt -DMESA_EGL_NO_X11_HEADERS --copt -DEGL_NO_X11 \
  mediapipe/examples/facial_search/desktop:facial_search \
  -- \
  --calculator_graph_config_file=mediapipe/examples/facial_search/graphs/facial_search.pbtxt \
  --images_folder_path=mediapipe/examples/facial_search/images/
```

Exit the program by pressing any key.

## Going from desktop to app
Tulsi can be used to [generate Xcode application projects](https://google.github.io/mediapipe/getting_started/ios.html#create-an-xcode-project) and Bazel can be used to [compile iOS apps from the command line](https://google.github.io/mediapipe/getting_started/ios.html#build-an-app-using-the-command-line). As iOS app developers we prefer to be able to import our graphs into our existing Xcode projects. We also plan to develop Android apps in the near future so we are betting on MediaPipe’s multiplatform support to reduce code duplication.

We designed an automated way to package our graphs as iOS frameworks. This runs as part of our Continuous Integration pipeline with macOS GitHub Actions and relies on Bazel and some scripting. Framework compilation and import being two separate steps, our mobile developers needn’t worry about the C++ and Objective-C part of the graphs and can build apps in Swift.

### General steps

1. **First, clone our example code:**
```sh
git clone --single-branch facial-search https://github.com/fenollp/mediapipe.git
cd mediapipe
```
1. **Create a new “Single View App” in Xcode**, setting language to Swift
1. **Delete these files from the new project:** (Move to Trash)
    * AppDelegate.swift
    * ViewController.swift
1. **Copy these files to your app** from `mediapipe/examples/facial_search/ios/`: (if asked, do not create a bridging header)
    * AppDelegate.swift
    * Cameras.swift
    * DotDot.swift
    * FacialSearchViewController.swift
1. **Edit your app’s `Info.plist`**:
    * Create key `NSCameraUsageDescription` with value: `This app uses the camera to demonstrate live video processing.`
1. **Edit your `Main.storyboard`’s custom class, setting it to `FacialSearchViewController`** (in the Identity inspector)
    * ![xcode identity inspector](./assets/sha256/5b2464b133f423fe2749429bb6b49aae0fca7d04e87d2d21958443d3a5cb8066.png)
1. **Build the iOS framework with**
```sh
bazel build --config=ios_arm64 \
     --copt=-fembed-bitcode --apple_bitcode=embedded \
     mediapipe/examples/facial_search/ios:FacialSearch
```
Some linker warnings about global C++ symbols may appear. <br>The flags `--copt=-fembed-bitcode --apple_bitcode=embedded` enable bitcode generation.
1. **Patch the Bazel product so it can be imported properly**:
```sh
./mediapipe/examples/facial_search/ios/patch_ios_framework.sh \
    bazel-bin/mediapipe/examples/facial_search/ios/FacialSearch.zip ObjcppLib.h
```
Note: append the contents of `FRAMEWORK_HEADERS` separated by spaces (here: `ObjcppLib.h`).
1. Open `bazel-bin/mediapipe/examples/facial_search/ios` and **drag and drop the `FacialSearch.framework` folder into your app files**
    * Copy items if needed > Finish
1. **Make sure the framework gets embedded into the app**.
    * In General > Frameworks, Libraries, and Embedded Content set `FacialSearch.framework` to `Embed & Sign`
    * ![xcode embed framework](./assets/sha256/980c03259583a263889e8deab1a8be703d2b7d092381f53d610eeac49280b3a4.png)
1. **Connect your device and run.**
    * Note the preprocessor statements at the top of `FacialSearchViewController.swift`:

```swift
import AVFoundation
import SceneKit
import UIKit

#if canImport(FacialSearch)
  // Either import standalone iOS framework...
  import FacialSearch

  func facialSearchBundle() -> Bundle {
    return Bundle(for: FacialSearch.self)
  }
#elseif canImport(mediapipe_examples_facial_search_ios_ObjcppLib)
  // ...or import the ObjcppLib target linked using Bazel.
  import mediapipe_examples_facial_search_ios_ObjcppLib

  func facialSearchBundle() -> Bundle {
    return Bundle.main
  }
#endif
```
There are two ways you can import our framework:
* If it was imported using the above technique just use
    * `import FacialSearch`
* If however you used Tulsi or Bazel to build the app you will have to use the longer form that reflects the Bazel target of the library the framework provides
    * `import mediapipe_examples_facial_search_ios_ObjcppLib`

### Why the need for `patch_ios_framework.sh`?
It turns out the Apple rules of Bazel do not yet generate importable iOS frameworks. This was just not the intended usage of **ios_framework**. There is however [an open issue](https://github.com/bazelbuild/rules_apple/issues/355) tracking the addition of this feature.

Our script is a temporary workaround that adds the umbrella header and modulemap that Bazel does not create. This lists the Objective-C headers of your framework as well as the iOS system libraries either your code or MediaPipe’s require to run.

## Conclusion
We built a machine learning inference graph that uses two Tensorflow Lite models, one provided by the MediaPipe team and one we developed at Powder.gg. Then discussed using subgraphs and creating our own MediaPipe calculators. Finally we described how to bundle our graph into an iOS framework that can readily be imported into other Xcode projects.

Here’s a link to [a GitHub repository with the code and assets mentioned](https://github.com/fenollp/mediapipe/tree/facial-search) in this post.

Here's [the corresponding pull request](https://github.com/google/mediapipe/pull/787) against upstream MediaPipe at Google.

*We sincerely hope you liked this tutorial and that it will help you on your way to create applications with MediaPipe.*
