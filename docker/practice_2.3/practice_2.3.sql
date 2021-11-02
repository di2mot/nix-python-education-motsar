-- TASK 1

CREATe TABLE potential_customers(
    Id SERIAL PRIMARY KEY,
    Name CHARACTER VARYING(30),
    Surname CHARACTER VARYING(30),
    Second_name CHARACTER VARYING(30),
    Email CHARACTER VARYING(30),
    City CHARACTER VARYING(30)
);

INSERT INTO potential_customers (Name, Surname, Second_name, Email, City)
VALUES ('Eli', 'Vance', 'Mc. Milan', 'caty@allies.org', 'City17'),
       ('Judith', 'Mossman', 'Doctor', 'mossman@combine.me', 'City17'),
       ('Barney ', 'Calhoun', 'Smith', 'barney@allies.org', 'City17'),
       ('Alyx', 'Vance', 'Smart', 'alyx@allies.org', 'City17'),
       ('Gordon', 'Freeman', 'Doctor', 'freeman@allies.org', 'City17'),
       ('first_name 17', 'middle_name 17', 'Noname', 'email17@gmail.com', 'City17'),
       ('Isaac ', 'Kleiner', 'Prat', 'isaac@allies.org', 'City17'),
       ('Father', 'Grigori', 'Saint', 'hell@allies.org', 'City17'),
       ('Dog ', 'BigDog', '010011011011', '1001001@allies.org', 'City17'),
       ('Vortigaunts', 'Q-Sht`j', 'Ch-k-t-q', 'asfq@alien.org', 'City17'),
       ('G', 'Man', 'Doctor', 'gman@org.org', 'City17'),
       ('first_name 17', 'middle_name 17', 'Noname', 'email17@gmail.com', 'City17');


/*-- TASK 2
 It`s  don`t work and I don`t now why.... Sad....*/
INSERT INTO users (first_name, last_name, middle_name, email, city, is_staff, password, country, address, phone_number)
VALUES ('Eli', 'Vance', 'Mc. Milan', 'caty@allies.org', 'City17', 0, '46845312', 'London', 'address 0', 080000000),
       ('Judith', 'Mossman', 'Doctor', 'mossman@combine.me', 'City17', 0, '46845312', 'London', 'address 0', 080000000),
       ('Barney ', 'Calhoun', 'Smith', 'barney@allies.org', 'City17', 0, '46845312', 'London', 'address 0', 080000000),
       ('Alyx', 'Vance', 'Smart', 'alyx@allies.org', 'City17', 0, '46845312', 'London', 'address 0', 080000000),
       ('Gordon', 'Freeman', 'Doctor', 'freeman@allies.org', 'City17', 0, '46845312', 'London', 'address 0', 080000000),
       ('first_name 17', 'middle_name 17', 'Noname', 'email17@gmail.com', 'City17', 0, '46845312', 'London', 'address 0', 080000000),
       ('Isaac ', 'Kleiner', 'Prat', 'isaac@allies.org', 'City17', 0, '46845312', 'London', 'address 0', 080000000),
       ('Father', 'Grigori', 'Saint', 'hell@allies.org', 'City17', 0, '46845312', 'London', 'address 0', 080000000),
       ('Dog ', 'BigDog', '010011011011', '1001001@allies.org', 'City17', 0, '46845312', 'London', 'address 0', 080000000),
       ('Vortigaunts', 'Q-Sht`j', 'Ch-k-t-q', 'asfq@alien.org', 'City17', 0, '46845312', 'London', 'address 0', 080000000),
       ('G', 'Man', 'Doctor', 'gman@org.org', 'City17', 0, '46845312', 'London', 'address 0', '080000000'),
       ('first_name 17', 'middle_name 17', 'Noname', 'email17@gmail.com', 'City17', 0, '46845312', 'London', 'address 0', 080000000);

-- It`s doesn`t work too
INSERT INTO users (email, password, first_name, last_name, middle_name, is_staff, country, city, address, phone_number)
VALUES ('city@allies.org', '486413518464131', 'Eli', 'Vance', 'Mc. Milan', 0, 'Mad word', 'City17', 'address 0', '080000000');

-- It`s work
UPDATE users
SET (email, password, first_name, last_name, middle_name, is_staff, country, city, address, phone_number) =
('city@allies.org', '486413518464131', 'Eli', 'Vance', 'Mc. Milan', 0, 'Mad word', 'City17', 'address 0', '080000000')
WHERE user_id=500;
select * from users
WHERE user_id=500;



SELECT first_name AS name,
       email
FROM users
ORDER BY name, city;

-- TASK 3
SELECT c.category_description, count(category_id) from products
JOIN categories c
USING(category_id)
GROUP BY c.category_id
ORDER BY c.category_id;


--      TASK 4

/*Task 4.1
1. Вывести продукты, которые ни разу не попадали в корзину.*/

SELECT product_title
 FROM products
 WHERE product_id NOT IN (SELECT products_product_id FROM cart_products);

/* Task 4.2
2. Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину попасть могли). */
SELECT product_title
 FROM products
 WHERE product_id NOT IN (
     SELECT products_product_id
     FROM cart_products
     WHERE cart_cart_id NOT IN (
         SELECT cart_id FROM carts));

/*Task 4.3
3. Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.*/
SELECT p.product_title
from products p
JOIN cart_products c
    ON p.product_id = c.products_product_id
    GROUP BY p.product_id
    ORDER BY p.product_id
    LIMIT 10;

/*Task 4.4
4. Вывести топ 10 продуктов, которые не только добавляли в корзины, но и оформляли заказы чаще всего.*/
SELECT p.product_title
FROM products p
JOIN cart_products cp
    ON p.product_id = cp.products_product_id
JOIN carts c
    ON cp.cart_cart_id = c.cart_id
JOIN orders o
    ON c.cart_id = o.cart_cart_id
    ORDER BY o.cart_cart_id
    LIMIT 5;

/*Task 4.5
5. Вывести топ 5 юзеров, которые потратили больше всего денег (total в заказе).*/
SELECT u.first_name
from users u
JOIN carts c on u.user_id = c.users_uses_id
WHERE u.user_id in (
    SELECT users_uses_id
    from carts
    where cart_id in (
        select cart_cart_id
        from orders
        ORDER BY total
        DESC LIMIT 5));


/*Task 4.6
6. Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).*/
SELECT users_uses_id
from carts
where cart_id in (
    SELECT cart_cart_id
    FROM orders
    ORDER BY total
    LIMIT 5);


/*Task 4.7
7. Вывести топ 5 юзеров, которые создали корзины, но так и не сделали заказы*/

SELECT users_uses_id
from carts
where cart_id not in (
    SELECT cart_cart_id
    FROM orders
    ORDER BY total
    LIMIT 5);