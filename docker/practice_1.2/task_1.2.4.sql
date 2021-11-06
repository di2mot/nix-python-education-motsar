/*
 Задание 4
Создать 2 функции (одна из них должна возвращать таблицу, одна из них должна использовать циклы,
 одна из них должна использовать курсор
 */

begin;
create or replace function users_phone (user_id_phone int)
returns table (
  phone varchar)
language plpgsql
as $$
declare
    var_r record;
begin
  for var_r in (
            select ('+'||pc.code::text || p.phone_number::text) as user_phone from customer c
        join phone p on c.phone_phone_id = p.phone_id
        join phone_code pc on p.phone_code_code_id = pc.code_id
        where c.cars_car_id = user_id_phone)
      loop
                phone := var_r.user_phone;
           return next;
  end loop;
end; $$;
select users_phone(53);
rollback;
commit;


 -- Cursors
begin;
create or replace function get_all_users(o_price integer)
   returns text as $$
declare
	 titles text default '';
	 full_price   record;
	 cur_price cursor(o_price integer)
		 for select c.first_name as name, price
		 from "practice_1.2".public.orders
		 join customer c on c.user_id = orders.customer_user_id
		 where price between (o_price-100)::money and (o_price+100)::money;
begin
   -- open the cursor
   open cur_price(o_price);
   titles := 'price: ';

   loop

      fetch cur_price into full_price;

      exit when not found;

      if full_price.name ilike 'name%' then
         titles := titles || ',' || full_price.name || ':' || full_price.price;
      end if;
   end loop;

   -- close the cursor
   close cur_price;
   return titles;
end; $$
language plpgsql;

select get_all_users(2500);
select * from customer;
rollback ;