/*
 Задание 5
Написать 2 любые хранимые процедуры. В них использовать транзакции для insert, update, delete.
*/

create table rich_customer(
  user_id serial primary key not null,
  best_buy money  not null
);

-- procedure 1

BEGIN;
    CREATE OR REPLACE PROCEDURE new_fu()
    LANGUAGE plpgsql
    AS $$
        DECLARE
            var record;
        BEGIN
            FOR var in
                select distinct  customer_user_id,
                                max(price) over (partition by customer_user_id) as max
                from orders
                LIMIT 10
            loop
                if var.max = 100::money  THEN
                    RAISE NOTICE 'Error';
                    ROLLBACK;
                end if;
                -- INSERT
                insert into rich_customer(best_buy) values(var.max);
                -- UPDATE
                update orders set price = 0::money where customer_user_id = var.customer_user_id
            end loop;
        end;
    $$;
CALL new_fu();
select * from rich_customer;
select * from orders;
rollback;
commit;


-- procedure 2

BEGIN;
    CREATE OR REPLACE PROCEDURE del_fu()
    LANGUAGE plpgsql
    AS $$
        DECLARE
            var record;
        BEGIN
            FOR var in
                select  customer_user_id as users, count(customer_user_id) as amount
                from "practice_1.2".public.orders
                group by customer_user_id
            loop
                if var.amount = 1  THEN
                    RAISE NOTICE 'Error';
                    ROLLBACK;
                end if;
                -- INSERT
                delete from orders where customer_user_id = var.users;
            end loop;
        end;
    $$;
CALL del_fu();
select * from orders;
rollback;
commit;