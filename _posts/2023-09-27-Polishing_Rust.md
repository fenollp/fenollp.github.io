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
