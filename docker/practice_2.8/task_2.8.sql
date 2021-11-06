/*
1. Compare the price of each product n with the average price of products in the category
product n. Use window function. The result table should
contain the following columns: category_title, product_title, price, avg.
2. Add any 2 triggers and handlers to them, use transactions.
 */

-- Task 1

BEGIN;

select c.category_title, product_title, price,
       round((AVG(price) over (partition by p.category_id))::numeric, 4) as midle_price
from products p
    left join categories c on p.category_id = c.category_id
    ORDER BY p.category_id, p.product_id;

ROLLBACK ;
COMMIT;
-- Task 2. Добавить 2 любых триггера и обработчика к ним, использовать транзакции.

begin;

create table logging_products (
    rec_id serial primary key,
    product_id smallint references products(product_id),
    action VARCHAR(20),
    old_title VARCHAR(255),
    old_description VARCHAR(255),
    old_in_stock smallint,
    old_price float,
    old_slug VARCHAR(255),
    old_category smallint
);

DROP TABLE  logging_products;
SAVEPOINT create_table;

create or replace function logging_func()
    returns trigger
    language plpgsql
as
    $$
    BEGIN
        if NEW.product_title <> OLD.product_title or
           NEW.product_description <> OLD.product_description or
           NEW.in_stock <> OLD.in_stock or
           NEW.price <> OLD.price or
           NEW.slug <> OLD.slug or
           NEW.category_id <> OLD.category_id
            THEN
            insert into logging_products(product_id, action,  old_title, old_description, old_in_stock, old_price, old_slug, old_category)
            VALUES(OLD.product_id, 'update', OLD.product_title, OLD.product_description, OLD.in_stock, OLD.price, OLD.slug, OLD.category_id);
        end if;
        RETURN NEW;
end; $$;

ROLLBACK;

CREATE TRIGGER logigng_update_products
  BEFORE UPDATE
  ON products
  FOR EACH ROW
  EXECUTE PROCEDURE logging_func();

UPDATE products
SET price=200
WHERE product_id=1;

select * from products;
select * from logging_products;

ROLLBACK;
COMMIT;

begin;
create or replace function alert_delete()
returns trigger
language plpgsql
as
    $$
    BEGIN
        insert into logging_products(product_id, action)
        VALUES(OLD.product_id, 'delete');
        RAISE NOTICE 'Attention, the entry % has been deleted',  OLD.product_id;
    end;
    $$;

CREATE TRIGGER loggigng_delete_products
  BEFORE DELETE
  ON products
  FOR EACH ROW
  EXECUTE PROCEDURE alert_delete();

delete  from products
where product_id = 2;

select * from logging_products;

rollback;
commit;

