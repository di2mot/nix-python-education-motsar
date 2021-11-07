/*
Задание 2
Придувать 3 различных запроса SELECT с осмысленным использованием разных видов JOIN.
Используя explain добавить только необходимые индексы для уменьшения стоимости (cost) запросов.
 */

/*
 Sort  (cost=101.03..101.03 rows=3 width=56) (actual time=2.586..2.590 rows=2 loops=1)
  Sort Key: (EXTRACT(day FROM (o.renting_period - o.renting_day))) DESC
  Sort Method: quicksort  Memory: 25kB
  ->  Nested Loop  (cost=22.80..101.00 rows=3 width=56) (actual time=0.604..2.571 rows=2 loops=1)
        ->  Hash Join  (cost=22.52..100.05 rows=3 width=40) (actual time=0.507..2.466 rows=2 loops=1)
              Hash Cond: (o.customer_user_id = c.user_id)
              ->  Seq Scan on orders o  (cost=0.00..74.00 rows=1340 width=36) (actual time=0.022..1.880 rows=1344 loops=1)
                    Filter: (EXTRACT(day FROM (renting_period - renting_day)) > '0'::numeric)
                    Rows Removed by Filter: 1456
              ->  Hash  (cost=22.50..22.50 rows=2 width=12) (actual time=0.311..0.312 rows=2 loops=1)
                    Buckets: 1024  Batches: 1  Memory Usage: 9kB
                    ->  Seq Scan on customer c  (cost=0.00..22.50 rows=2 width=12) (actual time=0.063..0.304 rows=2 loops=1)
                          Filter: ((second_name)::text = 'second_name 200'::text)
                          Rows Removed by Filter: 998
        ->  Index Scan using products_pkey on products p  (cost=0.27..0.31 rows=1 width=8) (actual time=0.046..0.046 rows=1 loops=2)
              Index Cond: (product_id = o.products_product_id)
Planning Time: 0.619 ms
Execution Time: 2.656 ms

 */


EXPLAIN (ANALYSE) select c.first_name, o.order_id, p.cars_car_id, o.price,
       extract(day from o.renting_period - o.renting_day) AS days
from orders o
join customer c
on c.user_id=o.customer_user_id
join products p on o.products_product_id=p.product_id
where extract(day from o.renting_period - o.renting_day) between 0 and 100 and c.second_name='second_name 500'
ORDER BY days DESC;

create index on "customer"(second_name);
create index on "orders"(extract(day from renting_period - renting_day));

/*
 Sort  (cost=85.99..86.00 rows=2 width=56) (actual time=0.889..0.893 rows=1 loops=1)
  Sort Key: (EXTRACT(day FROM (o.renting_period - o.renting_day))) DESC
  Sort Method: quicksort  Memory: 25kB
  ->  Nested Loop  (cost=38.43..85.98 rows=2 width=56) (actual time=0.438..0.882 rows=1 loops=1)
        ->  Hash Join  (cost=38.16..85.32 rows=2 width=40) (actual time=0.426..0.869 rows=1 loops=1)
              Hash Cond: (o.customer_user_id = c.user_id)
              ->  Bitmap Heap Scan on orders o  (cost=28.50..73.55 rows=802 width=36) (actual time=0.295..0.636 rows=808 loops=1)
                    Recheck Cond: ((EXTRACT(day FROM (renting_period - renting_day)) >= '0'::numeric) AND (EXTRACT(day FROM (renting_period - renting_day)) <= '100'::numeric))
                    Heap Blocks: exact=25
                    ->  Bitmap Index Scan on orders_extract_idx  (cost=0.00..28.30 rows=802 width=0) (actual time=0.279..0.279 rows=808 loops=1)
                          Index Cond: ((EXTRACT(day FROM (renting_period - renting_day)) >= '0'::numeric) AND (EXTRACT(day FROM (renting_period - renting_day)) <= '100'::numeric))
              ->  Hash  (cost=9.63..9.63 rows=2 width=12) (actual time=0.050..0.051 rows=2 loops=1)
                    Buckets: 1024  Batches: 1  Memory Usage: 9kB
                    ->  Bitmap Heap Scan on customer c  (cost=4.29..9.63 rows=2 width=12) (actual time=0.038..0.044 rows=2 loops=1)
                          Recheck Cond: ((second_name)::text = 'second_name 500'::text)
                          Heap Blocks: exact=2
                          ->  Bitmap Index Scan on customer_second_name_idx  (cost=0.00..4.29 rows=2 width=0) (actual time=0.027..0.027 rows=2 loops=1)
                                Index Cond: ((second_name)::text = 'second_name 500'::text)
        ->  Index Scan using products_pkey on products p  (cost=0.27..0.32 rows=1 width=8) (actual time=0.004..0.005 rows=1 loops=1)
              Index Cond: (product_id = o.products_product_id)
Planning Time: 0.757 ms
Execution Time: 0.973 ms

 */

/* -----------------------------------------tack 2------------------------------------------------ */
/*
Hash Join  (cost=162.36..225.92 rows=6 width=10) (actual time=2.767..4.006 rows=8 loops=1)
  Hash Cond: (o.products_product_id = p.product_id)
  ->  Seq Scan on orders o  (cost=0.00..53.00 rows=2800 width=4) (actual time=0.010..0.593 rows=2800 loops=1)
  ->  Hash  (cost=162.35..162.35 rows=1 width=14) (actual time=2.632..2.637 rows=2 loops=1)
        Buckets: 1024  Batches: 1  Memory Usage: 9kB
        ->  Hash Right Join  (cost=138.59..162.35 rows=1 width=14) (actual time=2.203..2.633 rows=2 loops=1)
              Hash Cond: (c2.cars_car_id = c.car_id)
              ->  Seq Scan on customer c2  (cost=0.00..20.00 rows=1000 width=4) (actual time=0.014..0.375 rows=1000 loops=1)
              ->  Hash  (cost=138.57..138.57 rows=1 width=18) (actual time=1.959..1.963 rows=1 loops=1)
                    Buckets: 1024  Batches: 1  Memory Usage: 9kB
                    ->  Hash Join  (cost=129.26..138.57 rows=1 width=18) (actual time=1.835..1.960 rows=1 loops=1)
                          Hash Cond: (p.cars_car_id = c.car_id)
                          ->  Seq Scan on products p  (cost=0.00..8.00 rows=500 width=8) (actual time=0.013..0.124 rows=500 loops=1)
                          ->  Hash  (cost=129.25..129.25 rows=1 width=14) (actual time=1.697..1.699 rows=1 loops=1)
                                Buckets: 1024  Batches: 1  Memory Usage: 9kB
                                ->  Seq Scan on cars c  (cost=0.00..129.25 rows=1 width=14) (actual time=0.068..1.691 rows=1 loops=1)
                                      Filter: ((car_plate)::text = '1e28332ad'::text)
                                      Rows Removed by Filter: 6499
Planning Time: 0.882 ms
Execution Time: 4.077 ms
 */
EXPLAIN (ANALYSE) select c.car_plate from products as p
right join cars c on c.car_id=p.cars_car_id
join "practice_1.2".public.orders o on o.products_product_id=p.product_id
left join customer c2 on c.car_id = c2.cars_car_id
where  c.car_plate = '1e28332ad';

create index on "cars"(car_plate);
--drop index cars_car_plate_idx1;

/*
 Hash Join  (cost=40.85..104.41 rows=6 width=10) (actual time=0.980..2.260 rows=8 loops=1)
  Hash Cond: (o.products_product_id = p.product_id)
  ->  Seq Scan on orders o  (cost=0.00..53.00 rows=2800 width=4) (actual time=0.009..0.636 rows=2800 loops=1)
  ->  Hash  (cost=40.84..40.84 rows=1 width=14) (actual time=0.846..0.850 rows=2 loops=1)
        Buckets: 1024  Batches: 1  Memory Usage: 9kB
        ->  Hash Join  (cost=30.95..40.84 rows=1 width=14) (actual time=0.720..0.847 rows=2 loops=1)
              Hash Cond: (p.cars_car_id = c.car_id)
              ->  Seq Scan on products p  (cost=0.00..8.00 rows=500 width=8) (actual time=0.011..0.124 rows=500 loops=1)
              ->  Hash  (cost=30.94..30.94 rows=1 width=14) (actual time=0.590..0.592 rows=2 loops=1)
                    Buckets: 1024  Batches: 1  Memory Usage: 9kB
                    ->  Hash Right Join  (cost=8.31..30.94 rows=1 width=14) (actual time=0.192..0.589 rows=2 loops=1)
                          Hash Cond: (c2.cars_car_id = c.car_id)
                          ->  Seq Scan on customer c2  (cost=0.00..20.00 rows=1000 width=4) (actual time=0.009..0.242 rows=1000 loops=1)
                          ->  Hash  (cost=8.30..8.30 rows=1 width=14) (actual time=0.050..0.051 rows=1 loops=1)
                                Buckets: 1024  Batches: 1  Memory Usage: 9kB
                                ->  Index Scan using cars_car_plate_idx on cars c  (cost=0.28..8.30 rows=1 width=14) (actual time=0.043..0.044 rows=1 loops=1)
                                      Index Cond: ((car_plate)::text = '1e28332ad'::text)
Planning Time: 1.080 ms
Execution Time: 2.330 ms
 */

/*
 Hash Join  (cost=32.50..113.79 rows=110 width=16) (actual time=0.809..1.880 rows=90 loops=1)
  Hash Cond: (o.customer_user_id = c.user_id)
  ->  Seq Scan on orders o  (cost=0.00..81.00 rows=110 width=12) (actual time=0.019..1.037 rows=90 loops=1)
        Filter: ((price >= (1500)::money) AND (price <= (1800)::money))
        Rows Removed by Filter: 2710
  ->  Hash  (cost=20.00..20.00 rows=1000 width=12) (actual time=0.769..0.770 rows=1000 loops=1)
        Buckets: 1024  Batches: 1  Memory Usage: 55kB
        ->  Seq Scan on customer c  (cost=0.00..20.00 rows=1000 width=12) (actual time=0.013..0.393 rows=1000 loops=1)
Planning Time: 0.679 ms
Execution Time: 1.942 ms

 */

EXPLAIN (ANALYSE) select c.first_name, o.price from orders as o
join customer c on c.user_id = o.customer_user_id
where o.price between 1500::money and 1800::money;

create index on "orders"(price);
drop index orders_price_idx;

/*
 Hash Join  (cost=37.91..65.40 rows=110 width=16) (actual time=0.774..0.911 rows=90 loops=1)
  Hash Cond: (o.customer_user_id = c.user_id)
  ->  Bitmap Heap Scan on orders o  (cost=5.41..32.61 rows=110 width=12) (actual time=0.051..0.131 rows=90 loops=1)
        Recheck Cond: ((price >= (1500)::money) AND (price <= (1800)::money))
        Heap Blocks: exact=22
        ->  Bitmap Index Scan on orders_price_idx  (cost=0.00..5.39 rows=110 width=0) (actual time=0.035..0.035 rows=90 loops=1)
              Index Cond: ((price >= (1500)::money) AND (price <= (1800)::money))
  ->  Hash  (cost=20.00..20.00 rows=1000 width=12) (actual time=0.709..0.710 rows=1000 loops=1)
        Buckets: 1024  Batches: 1  Memory Usage: 55kB
        ->  Seq Scan on customer c  (cost=0.00..20.00 rows=1000 width=12) (actual time=0.013..0.347 rows=1000 loops=1)
Planning Time: 0.434 ms
Execution Time: 0.972 ms

 */