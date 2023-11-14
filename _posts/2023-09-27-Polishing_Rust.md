---
wip: true
title: Polishing Rust
layout: post
categories: [projects]
permalink: Polishing_Rust
---

* `diesel` compile time fail when `update` without setting `updated_at` field
* ensure `no_copy` macro attribute
* look for a way to disallow usage of the `eq` method on `Nullable` values and suggest `query.filter(dsl::zone_id.is_not_distinct_from(req.zone_id));`
* diesel ensure all queries are explicitly `order`ed
* rust macro bang to return ok `a.b.c!`: `a.b.c.map(Ok)`
* diesel struct fields ordering matters even with name+`sql_type` but not without `table_name` annotation
* write cobol in rust
* rust diesel color conn with readonly
* rust clippy `let keys = devices.keys().copied().collect::<Vec<_>>();for key in keys {`
* `no_panic` introduce a new unique libpanic.so, cardinality tuned for precision on codebase origin. build.rs generates uniq crates copying libpanic.so code but with uniq final .so files
* haxl in rust (i.e. compile-time errors when interleaving the use of >1 resources. E.g. DB conn + gRPC calls => put back conn to pool)
* attribute macro on `diesel`'s user structs (returned by `load`, `get_result`, `get_results`, ...) that `impl Drop` and says `"oh gee, we're dropping something we mutated but didn't write back to DB hmmm?"`  (attr adds a new private int struct field that stores which fields were modified)

* [SIMD Floating point and integer compressed vector library](https://github.com/velvia/compressed-vec)
	* generalize-able SIMD-oriented `Iterator`
	* https://github.com/velvia/compressed-vec/blob/main/src/sink.rs
	* https://github.com/velvia/compressed-vec/blob/81f6f7aa9d2935b234ac92d47a17ecd82c569baf/src/vector.rs#L460
	* https://github.com/velvia/compressed-vec/blob/81f6f7aa9d2935b234ac92d47a17ecd82c569baf/src/section.rs#L349


<!-- 
# Colorless async in Rust

Sprinkling async/.await some places is suboptimal when done by humans, let's turn it around!

Could be introduced in a new edition.

### Common use

 /// Count ips booked in Private Networks in current region.
-async fn count_ips(ctx: &Ctx, pn_ids: &[Uuid]) -> Result<usize> {
+fn count_ips(ctx: &Ctx, pn_ids: &[Uuid]) -> Result<usize> {
     iter(repeat(ctx.ipam_api()).zip(pn_ids))
-        .map(|(mut ipam, pn_id)| async move { ipam.count_ips(*pn_id).await })
+        .map(|(mut ipam, pn_id)| move { ipam.count_ips(*pn_id) })
         .boxed() // https://github.com/rust-lang/futures-rs/issues/2636#issuecomment-1242928098
         .buffered(10)
         .try_fold(0, |a, b| ok(a + b))
         .await
 }
ah but the move { .. }?
rustc complained just the same :)

### Using futures as values

```
api/tests/grpc/admin/book.rs-1179-async fn release_many(
api/tests/grpc/admin/book.rs-1180-    api: &IpamApiServer,
api/tests/grpc/admin/book.rs-1181-    token: String,
api/tests/grpc/admin/book.rs-1182-    ip_ids: Vec<(String, Option<GrpcResource>)>,
api/tests/grpc/admin/book.rs-1183-) -> (Vec<String>, Histogram) {
api/tests/grpc/admin/book.rs-1184-    let many = ip_ids.len();
api/tests/grpc/admin/book.rs-1185-
api/tests/grpc/admin/book.rs-1186-    let cntr = Arc::new(AtomicUsize::new(many));
api/tests/grpc/admin/book.rs:1187:    let handles = iter(ip_ids.into_iter())
api/tests/grpc/admin/book.rs-1188-        .map(|(ip_id, resource)| {
api/tests/grpc/admin/book.rs-1189-            let api = api.clone();
api/tests/grpc/admin/book.rs-1190-            let token = token.clone();
api/tests/grpc/admin/book.rs-1191-            let counter = cntr.clone();
api/tests/grpc/admin/book.rs-1192-            let req = ReleaseIpRequest { ip_id, resource };
api/tests/grpc/admin/book.rs-1193-            async move {
api/tests/grpc/admin/book.rs-1194-                let start = Utc::now().time();
api/tests/grpc/admin/book.rs-1195-                let response = api.release_ip(req_with_token(req.clone(), &token)).await;
api/tests/grpc/admin/book.rs-1196-                let elapsed = (Utc::now().time() - start).num_milliseconds();
api/tests/grpc/admin/book.rs-1197-                let counter = counter.fetch_sub(1, Ordering::Relaxed);
api/tests/grpc/admin/book.rs-1198-                eprintln!("{counter}: {elapsed}ms\t{response:?}");
api/tests/grpc/admin/book.rs-1199-                (response, elapsed)
api/tests/grpc/admin/book.rs-1200-            }
api/tests/grpc/admin/book.rs-1201-        })
api/tests/grpc/admin/book.rs-1202-        .map(tokio::spawn)
api/tests/grpc/admin/book.rs-1203-        .buffer_unordered(4 /*=worker_threads*/)
api/tests/grpc/admin/book.rs-1204-        .try_collect::<Vec<_>>();
api/tests/grpc/admin/book.rs-1205-
api/tests/grpc/admin/book.rs-1206-    let mut errs = Vec::with_capacity(many);
api/tests/grpc/admin/book.rs-1207-    let mut histogram = Histogram::new(7, 64).unwrap();
api/tests/grpc/admin/book.rs-1208-
api/tests/grpc/admin/book.rs-1209-    for (res, elapsed) in timeout(MAX_RUNTIME, handles)
api/tests/grpc/admin/book.rs-1210-        .await
api/tests/grpc/admin/book.rs-1211-        .map_err(|_: Elapsed| {
api/tests/grpc/admin/book.rs-1212-            eprintln!("Polling for {cntr:?}/{many} calls timed out after {MAX_RUNTIME:?}");
api/tests/grpc/admin/book.rs-1213-            exit(1) // Exit process because panic-ing does not end the test!
api/tests/grpc/admin/book.rs-1214-        })
api/tests/grpc/admin/book.rs-1215-        .unwrap()
api/tests/grpc/admin/book.rs-1216-        .unwrap()
api/tests/grpc/admin/book.rs-1217-    {
api/tests/grpc/admin/book.rs-1218-        histogram.increment(elapsed as u64).unwrap();
api/tests/grpc/admin/book.rs-1219-        if let Err(e) = res {
api/tests/grpc/admin/book.rs-1220-            errs.push(e.to_string())
api/tests/grpc/admin/book.rs-1221-        };
```
 -->

---


# Missing lints

## Prefer `.as_deref()` over `.clone()` when using just `.map(..)` on `Option<String>`

```rust
        let route = diesel::update(&route)
            .set((
                req.description.clone().map(|desc| route::description.eq(desc)),
                req.tags.clone().map(|tags| route::tags.eq(tags)),
                req.destination.map(|dest| route::destination.eq(dest)),
                req.nh_pn_id.map(|pn_id| route::nexthop_private_network_key.eq(pn_id)),
                req.nh_resource_id.map(|resource_id| route::nexthop_resource_key.eq(resource_id)),
                route::modification_date.eq(statement_timestamp()),
            ))
            .get_result::<Route>(conn)
            .with_resource("route", route.key)?;
```

    req.description.as_deref().map(|desc| route::description.eq(desc)),
    req.tags.as_deref().map(|tags| route::tags.eq(tags)),


## Redundant `Option<_>` check on `is_none()` with `unwrap_or_default()`

```rust
assert_eq!(
  user_input.as_ref().map(|x| !x.contains('@')).unwrap_or_default(),
  (user_input.is_none()
      || user_input.as_ref().map(|x| !x.contains('@')).unwrap_or_default()),
);
```


---


## Fix a design "angle mort" in `cargo`

Replace current (1.79) error:
```
error: the lock file $HOME/wefwefwef/reMarkable-tools.git/Cargo.lock needs to be updated but --locked was passed to prevent this
If you want to try to generate the lock file without accessing the network, remove the --locked flag and use --offline instead.
```
turn this error into "cargo-fetch then continue"


---


## downgrade owned argument to Ref


---


## An `async Drop` impl

```rust
impl Drop for Thing {
     fn drop(self) {
         let mut rt = ::tokio::runtime::Runtime::new().unwrap();
         rt.block_on(async { timeout(self.fd.close()).await.unwrap() });
     }
}

// Better yet!:
// > A correctly implemented runtime will run the destructor on that future,
// > allowing it to clean up its state.
```

```rust
// A proc-macro to make sure a Drop impl runs within reasonable ([statically] bounded) time

impl Drop for Thing {
    #[tokio::drop(timeout = "500ms")]
    async fn drop(self) {
        self.fd.close()
    }
}
```
>>>>>>> 4cd6100 (more thoughts on rust)
