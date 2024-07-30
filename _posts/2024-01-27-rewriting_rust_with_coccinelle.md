---
wip: true
title: rewriting rust with coccinelle
layout: post
categories: [projects, coccinelle]
permalink: rewriting_rust_with_coccinelle
---

https://twitter.com/josh_triplett/status/994753065478582272

https://github.com/rust-lang/rust-analyzer/issues/3186
https://www.google.com/search?channel=fs&client=ubuntu-sn&q=site%3Agithub.com++rust+semantic+patch+-semver

https://gitlab.inria.fr/coccinelle/coccinelleforrust

https://www.youtube.com/watch?v=Gh9lOyddqbY

https://users.rust-lang.org/t/we-need-a-great-general-refactoring-tool/103985/13


ohwow https://gitlab.inria.fr/lawall/patchparse4

### suggest better collection given apparent use

Notice an iterator looking into another one
If it's doing things a certain special way
Suggest a set impl so `O(n) --> O(1)`

```rust
 /// List FDB entries that are the result of a replication (i.e. on a veth)
 pub async fn list_replicated_macs(rtnl: &Netlink, links: &LinkMap) -> Result<Vec<FdbReplicated>> {
+    let link_macs = links.values().map(|link| link.mac).collect::<HashSet<_>>();
     let neighs = rtnl.get_bridge_neighs().await?;

     let neighs = neighs.into_iter().filter_map(|neigh| {
         // Ensure the neigh has a VLAN (or not, we don't care, it's just to deduplicate the neigh)
         neigh.vlan?;
         // Ignore MAC if it's the one of an interface itself
-        if links.values().any(|link| link.mac.as_slice() == neigh.mac) {
+        if link_macs.contains(&neigh.mac) {
             return None;
         }
         // Ignore multicast neighbors
         if neigh.is_multicast() {
             return None;
         }

         match links.get(&neigh.ifindex) {
             Some(Link::Veth(veth)) if veth.base.master.is_some() => {
                 Some((veth.base.index, neigh.mac))
             }
             _ => None,
         }
     });

     Ok(neighs.collect())
}
```

```rust
pub async fn list_replicated_macs(rtnl: &Netlink, links: &LinkMap) -> Result<Vec<FdbReplicated>> {
    // +    let link_macs = links.values().map(|link| link.mac).collect::<HashSet<_>>();
    let neighs = rtnl.get_bridge_neighs().await?;

    let neighs = neighs.into_iter().filter_map(|neigh| {
        // Ensure the neigh has a VLAN (or not, we don't care, it's just to deduplicate the neigh)
        neigh.vlan?;
        // Ignore MAC if it's the one of an interface itself
        if links.values().any(|link| link.mac.as_slice() == neigh.mac) {
            // +        if link_macs.contains(&neigh.mac) {
            return None;
        }
        // Ignore multicast neighbors
        if neigh.is_multicast() {
            return None;
        }

        match links.get(&neigh.ifindex) {
            Some(Link::Veth(veth)) if veth.base.master.is_some() => {
                Some((veth.base.index, neigh.mac))
            }
            _ => None,
        }
    });

    Ok(neighs.collect())
}
```

#### Attempt #1

```diff
@@
identifier c;
expression a, b, d;
@@

-    let a = b;
+    let a = b.iter().collect::<::std::collections::HashSet<_>>();

     ...

     for c in d {
         ...

-        if a.any(|x| x == c) {
+        if a.contains(&c) {
             ...
         }

         ...
     }
```

#### Attempt #2

```shell
cargo run --locked --frozen --offline --release -- --coccifile should_be_using_hashset.cocci src/should_be_using_hashset.rs
./target/release/cfr --coccifile should_be_using_hashset.cocci src/should_be_using_hashset.rs
```

```diff
@@
identifier xs, x, c;
expression items;
Iterator it;
@@

     let xs =
-             items;
+             items.iter().collect::<HashSet<_>>();

     ...

     it.filter_map(|x| {
         ...

         if xs.
-              any(|c| c == x)
+              contains(&x)
         {
             ...
         }

         ...
     })
```

---

```rust
#[test]
fn collecting_needlessly() {
    use std::collections::HashMap;

    let hmap = HashMap::from([('a', 42)]);
    for item in hmap.keys().copied().collect::<Vec<_>>() { // <--
        let _ = item;
    }
}
```

```diff
// cargo run --locked --frozen --offline --release -- --no-parallel --coccifile src/tests/needless_collect.cocci src/tests/needless_collect.rs

@@
Iterator it;
identifier x;
@@

     for x in it
-                 .copied().collect::<Vec<_>>()
     {
         ...
     }
```
