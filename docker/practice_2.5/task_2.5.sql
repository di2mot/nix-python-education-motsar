/*
 Practice 2.5

 Exercise:
Come up with 3 queries that can be optimized using an index (check
whether it is worth optimizing the query with the explain operator) and optimize them
using the index. Check the result also with the explain operator.

Include all queries in the final SQL file.
 */



BEGIN;
EXPLAIN (ANALYSE )SELECT * FROM imdb
WHERE country='USA'
    and genre='Comedy';
/*
Seq Scan on imdb  (cost=0.00..3538.82 rows=2527 width=188) (actual time=0.029..45.466 rows=2000 loops=1)
  Filter: (((country)::text = 'USA'::text) AND ((genre)::text = 'Comedy'::text))
  Rows Removed by Filter: 83855
Planning Time: 0.247 ms
Execution Time: 45.765 ms

 */
CREATE INDEX on "imdb"(country);
CREATE INDEX on "imdb"(genre);

EXPLAIN (ANALYSE )SELECT * FROM imdb
WHERE country='USA'
    and genre='Comedy';
/*
 Bitmap Heap Scan on imdb  (cost=348.09..3021.41 rows=2527 width=188) (actual time=3.253..23.984 rows=2000 loops=1)
  Recheck Cond: ((country)::text = 'USA'::text)
  Filter: ((genre)::text = 'Comedy'::text)
  Rows Removed by Filter: 26511
  Heap Blocks: exact=2212
  ->  Bitmap Index Scan on imdb_country_idx  (cost=0.00..347.46 rows=28155 width=0) (actual time=2.612..2.613 rows=28511 loops=1)
        Index Cond: ((country)::text = 'USA'::text)
Planning Time: 0.222 ms
Execution Time: 24.293 ms
 */

CREATE INDEX on "imdb"(genre);

EXPLAIN (ANALYSE )SELECT * FROM imdb
WHERE country='USA'
    and genre='Comedy';
/*
 Bitmap Heap Scan on imdb  (cost=90.73..2457.33 rows=2527 width=188) (actual time=1.943..11.158 rows=2000 loops=1)
  Recheck Cond: ((genre)::text = 'Comedy'::text)
  Filter: ((country)::text = 'USA'::text)
  Rows Removed by Filter: 5693
  Heap Blocks: exact=2132
  ->  Bitmap Index Scan on imdb_genre_idx  (cost=0.00..90.09 rows=7707 width=0) (actual time=1.338..1.339 rows=7693 loops=1)
        Index Cond: ((genre)::text = 'Comedy'::text)
Planning Time: 0.662 ms
Execution Time: 11.468 ms

 */
ROLLBACK;

BEGIN;

EXPLAIN (ANALYSE ) SELECT * FROM imdb
WHERE avg_vote > 7
AND year between 1980 and 1999;

/*
 Seq Scan on imdb  (cost=0.00..3753.46 rows=2659 width=188) (actual time=0.918..50.013 rows=2943 loops=1)
  Filter: ((avg_vote > '7'::double precision) AND (year >= 1980) AND (year <= 1999))
  Rows Removed by Filter: 82912
Planning Time: 0.169 ms
Execution Time: 50.396 ms

 */


CREATE INDEX on "imdb"(avg_vote);

EXPLAIN (ANALYSE ) SELECT * FROM imdb
WHERE avg_vote > 7
AND year between 1980 and 1999;

/*
 Bitmap Heap Scan on imdb  (cost=253.85..2739.98 rows=2659 width=188) (actual time=3.687..15.855 rows=2943 loops=1)
  Recheck Cond: (avg_vote > '7'::double precision)
  Filter: ((year >= 1980) AND (year <= 1999))
  Rows Removed by Filter: 10400
  Heap Blocks: exact=2208
  ->  Bitmap Index Scan on imdb_avg_vote_idx  (cost=0.00..253.19 rows=13436 width=0) (actual time=2.852..2.853 rows=13343 loops=1)
        Index Cond: (avg_vote > '7'::double precision)
Planning Time: 0.444 ms
Execution Time: 16.259 ms

 */

ROLLBACK;


BEGIN;

EXPLAIN (ANALYSE )  SELECT boxoffice from imbd_top
WHERE boxoffice>2000000::money;
/*
 Seq Scan on imbd_top  (cost=0.00..15.87 rows=70 width=8) (actual time=0.019..0.141 rows=70 loops=1)
  Filter: (boxoffice > (2000000)::money)
  Rows Removed by Filter: 121
Planning Time: 0.107 ms
Execution Time: 0.170 ms
 */
 CREATE INDEX on "imbd_top"(boxoffice);

EXPLAIN (ANALYSE )  SELECT boxoffice from imbd_top
WHERE boxoffice>2000000::money;

/*
 Index Only Scan using imbd_top_boxoffice_idx on imbd_top  (cost=0.15..5.37 rows=70 width=8) (actual time=0.042..0.059 rows=70 loops=1)
  Index Cond: (boxoffice > (2000000)::money)
  Heap Fetches: 0
Planning Time: 0.406 ms
Execution Time: 0.095 ms
 */

ROLLBACK;