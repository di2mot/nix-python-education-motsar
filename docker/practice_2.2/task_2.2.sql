-- TASK 1
SELECT u.first_name, p.product_title, o.status_name
FROM users u
inner join products p
    ON u.user_id=p.product_id
inner join order_status o
    ON p.product_id=o.order_status_id
ORDER BY u.first_name;

-- Task 1.1
SELECT * from users;


select user_id AS "ID",
       first_name AS "First name",
       last_name AS "Last name",
       middle_name AS "Midle name",
       phone_number AS "Phone number",
       email,
       password AS "Password",
       is_staff AS "Is staff",
       country as "Country",
       city AS "City",
       address AS "Adress"
from users;

-- Task 1.2
SELECT * from products;

-- Task 1.3
SELECT order_id,
       order_status_order_status_id AS status,
       shipping_total,
       total,
       create_at,
       update_at
FROM orders;

SELECT order_id,
       order_status_order_status_id AS status,
       shipping_total,
       total,
       create_at,
       update_at
FROM orders;

-- TASK 3

-- Task 3.1
SELECT product_title, price
FROM  products
WHERE price BETWEEN 80.00 and 150.00;

SELECT product_title, price
FROM  products
WHERE price > 80.00 and price <= 150.00;

-- Task 3.2
SELECT order_id, create_at
FROM orders
WHERE create_at >= '01-10-2020'::date;

-- Task 3.3
SELECT order_id, create_at
FROM orders
WHERE create_at BETWEEN '01-01-2020'::date
    and '01-06-2020'::date
and order_status_order_status_id = 1;


SELECT order_id, create_at,
       order_status_order_status_id AS order_status
FROM orders
WHERE create_at BETWEEN '01-01-2020'::date
    and '06-01-2020'::date
and order_status_order_status_id = 1;


SELECT o.order_id, o.create_at,
       os.status_name AS order_status
FROM orders AS o
JOIN order_status os on o.order_status_order_status_id = os.order_status_id
WHERE create_at BETWEEN '01-01-2020'::date
    and '07-01-2020'::date
and order_status_order_status_id = 1;

-- Task 3.4
SELECT product_title, category_id
FROM products
WHERE category_id = 7
OR category_id = 11
OR category_id = 18;


-- Task 3.5
SELECT order_id, update_at,
       order_status_order_status_id AS order_status
FROM orders
WHERE order_status_order_status_id = 3
    and update_at < '12-31-2020'::date;

SELECT o.order_id, o.update_at, os.status_name
FROM orders AS o
JOIN order_status os ON os.order_status_id = o.order_status_order_status_id
WHERE order_status_order_status_id = 3
    and update_at < '12-31-2020'::date;

-- Task 3.6
SELECT o.cart_cart_id, os.status_name
FROM orders AS o
JOIN order_status os ON os.order_status_id = o.order_status_order_status_id
WHERE order_status_order_status_id = 2;

-- TASK 4 --
-- TAsk 4.1
SELECT AVG(total) AS Average_Price
FROM orders
WHERE order_status_order_status_id = 4;
select * from orders;


-- TAsk 4.2
SELECT order_id, total
FROM orders
WHERE create_at BETWEEN '06-01-2020'::date
    AND '09-07-2020'::date AND
      order_status_order_status_id = 4
    AND total = (select MAX(total)
                FROM orders
                WHERE create_at BETWEEN '06-01-2020'::date
                    AND '09-07-2020'::date AND
                    order_status_order_status_id = 4);

select * from orders;
select * from order_status;