/*
Exercise:
1. Create a function that sets shipping_total = 0 in the order table if the user's city is x.
  Use IF clause.
2. Write any 2 stored procedures using conditions, loops and transactions.
 */

-- Task 1
CREATE OR REPLACE FUNCTION order_shipping(city_name VARCHAR)
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var_r record;
    BEGIN
        for var_r in
            select u.city, c.cart_id
            from orders o
            JOIN carts c on o.cart_cart_id = c.cart_id
            JOIN users u on c.users_uses_id = u.user_id
            --WHERE u.city = city_name
        loop
            IF var_r.city=city_name THEN
                UPDATE orders
                SET shipping_total=0
                WHERE cart_cart_id=var_r.cart_id;
            END IF;
        END loop;
        RETURN var_r;
    END;
$$;

-- For test
DROP FUNCTION order_shipping(city_name VARCHAR);
SELECT order_shipping('city 17');
SELECT * from orders where shipping_total=0;

-- Task 2
BEGIN;
    CREATE OR REPLACE PROCEDURE new_pas()
    LANGUAGE plpgsql
    AS $$
        DECLARE
            new_pas VARCHAR;
            var record;
        BEGIN
            FOR var in
                SELECT password, user_id
                FROM users
            loop
                if length(var.password) < 12 THEN
                    new_pas = (SELECT md5(random()::text));
                    UPDATE users
                    SET password = new_pas
                    WHERE length(var.password)  < 11;
                    RAISE NOTICE 'users % password too simple. New password: %', var.user_id, new_pas;
                end if;
            end loop;
        end;
    $$;

-- Test
    CALL new_pas();
    SELECT * FROM users;
ROLLBACK ;


BEGIN;
    CREATE OR REPLACE PROCEDURE new_fu()
    LANGUAGE plpgsql
    AS $$
        DECLARE
            var record;
        BEGIN
            FOR var in
                SELECT user_id
                FROM users
            loop
                if var.user_id::int % 3 = 0 and  var.user_id::int % 5 = 0 THEN
                    RAISE NOTICE 'FIZZBUZZ';
                end if;
                if var.user_id::int % 3 = 0 and  var.user_id::int % 5 <> 0 THEN
                    RAISE NOTICE 'FIZZ';
                end if;
                if var.user_id::int % 5 = 0  and var.user_id::int % 3 <> 0 THEN
                    RAISE NOTICE 'BUZZ';
                end if;
                if var.user_id::int > 100  THEN
                    RAISE NOTICE 'Too much users!';
                    ROLLBACK;
                end if;
            end loop;
        end;
    $$;

-- Test
CALL new_fu();
DROP PROCEDURE new_fu();
ROLLBACK;