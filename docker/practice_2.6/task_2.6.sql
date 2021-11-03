/*
Exercise:
Write 3 views for the product table, for the order_status and order tables, and for the products and category tables.
Create a materialized view for a "heavy" query at your own discretion.
Remember to make requests to remove views.
 */


BEGIN;

    CREATE VIEW products_stock AS
        SELECT product_id,  product_title, in_stock
        FROM products
        WHERE in_stock > 10
        ORDER BY in_stock DESC
        LIMIT 10
        WITH LOCAL CHECK OPTION;

    SELECT * FROM products_stock;
    DROP VIEW products_stock;

ROLLBACK;
SAVEPOINT part_1;


    CREATE VIEW order_order_status AS
        SELECT order_id, os.status_name
        FROM orders
            JOIN order_status os
                ON orders.order_status_order_status_id = os.order_status_id;

SELECT * FROM  order_order_status;
DROP VIEW  order_order_status;

ROLLBACK;
SAVEPOINT part_2;


    CREATE VIEW order_cart AS
        SELECT o.order_id, subtotal
        FROM carts
        JOIN orders o on carts.cart_id = o.cart_cart_id
        ORDER BY subtotal DESC;

SELECT * FROM order_cart;

ROLLBACK;
SAVEPOINT part_3;

    CREATE MATERIALIZED VIEW rental_by_category
        AS
            SELECT o.order_id, o.total, u.first_name
            FROM carts
            JOIN orders o on carts.cart_id = o.cart_cart_id
            JOIN users u on carts.users_uses_id = u.user_id
        WITH NO DATA;

REFRESH MATERIALIZED VIEW rental_by_category;

SELECT * FROM rental_by_category;

ROLLBACK;
COMMIT;

