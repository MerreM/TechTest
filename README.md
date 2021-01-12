# Technical Test

Quick and (hopefully) not too dirty solution to the Dev task.

Tools used - Sublime, python3.8, sqlite, postgres

## Quick info

There's a dirty hack in the settings.py file line 88 to switch databases for the compose environment.

Normally I'd put env settings in different files, but that's a demo of the functionaility.

Run locally (without DOCKER_COMPOSE=1 env) you will use a SQlite database. Good for unit testing etc.

## Tasks

These shuold be demoed by the the unit tests.

./stock/tests.py

1) Register a product <- test_create_stock
2) Retrieve Product Details from SKU <- test_get_cheese_by_sku
3) List all available products (>0 Qty) <- test_query_quantity_in_stock
4) List all sold out products (0 Qty) <- test_query_quantity
5) Register Qty Change (SKU, +/- Value) <- test_update_cheese_quantity and test_reduce_cheese_quantity

NB Not a *huge* fan of the way that the `update_quantity` got implemented in the end. But "PATCH" didn't seem appropriate.


