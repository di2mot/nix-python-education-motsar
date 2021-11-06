/*
 Задание 6
Добавить 2 триггера (один из них ДО операции по изменению данных, второй после) и
функции или процедуры-обработчики к ним.
 */

-- trigger 1
begin;
create or replace function ban_on_deletion()
    returns trigger
    language plpgsql
as
    $$
    BEGIN
        raise 'You cannot delete users';
end; $$;

ROLLBACK;

CREATE TRIGGER alert_deleting
  BEFORE DELETE
  ON customer
  FOR EACH ROW
  EXECUTE PROCEDURE ban_on_deletion();

DELETE from customer where user_id = 1;

ROLLBACK;
COMMIT;


-- trigger 2
create table if not exists price_safer (
    operating_id serial primary key not null,
    product_product_id int,
    old_price money not null ,
    new_price money not null,
    editing_time timestamp
);
--drop table  price_safer;

begin;
create or replace function check_update_function()
returns trigger
language plpgsql
as
    $$
    BEGIN
        if OLD.price <> NEW.price THEN
            insert into price_safer(product_product_id, old_price, new_price, editing_time)
            VALUES(old.products_product_id, old.price, new.price, now());
            end if;
        RETURN NEW;
    end;
    $$;

CREATE TRIGGER check_update
  AFTER UPDATE
  ON orders
  FOR EACH ROW
  EXECUTE PROCEDURE check_update_function();

select * from orders;
select * from price_safer;

update orders
    set price = 1000
    where customer_user_id = 1;
rollback;
commit;