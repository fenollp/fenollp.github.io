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


---

rust clippy coccinelle

## suggest better collection given apparent use

Notice an iterator looking into another one
If it's doing things a certain special way
Suggest a set impl

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



---


# rust best async UX

## A new edition that changes async sugar

Sprinkling async/.await some places is suboptimal when done by humans, let's turn it around!

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

