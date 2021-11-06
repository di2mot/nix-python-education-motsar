/*
 Задание 3
Создать 3 представления (1 из них должно быть материализированным и хранить данные от "тяжелого" запроса).
 */

 begin;
     CREATE VIEW order_prise AS
        SELECT c.first_name, o.price
        FROM orders as o
            JOIN customer c
                ON o.customer_user_id=c.user_id;
select * from order_prise;
commit;

 begin;
     CREATE VIEW customer_phones AS
        select c.first_name, '+'||pc.code::text || p.phone_number::text from customer c
        join phone p on c.phone_phone_id = p.phone_id
        join phone_code pc on p.phone_code_code_id = pc.code_id;

select * from customer_phones;
commit;

begin;
    CREATE MATERIALIZED VIEW customer_full_info
        AS
            select c.first_name, c.second_name,
               ('+'||pc.code::text || p.phone_number::text) as phone,
               st.stage_name, ct.city_name, s.street_name
        from customer c
        join phone p on c.phone_phone_id = p.phone_id
        join phone_code pc on p.phone_code_code_id = pc.code_id
        join address a on c.address_address_id = a.address_id
        join city ct on a.city_city_id = ct.city_id
        join street s on a.street_street_id = s.street_id
        join stage st on a.stage_stage_id = st.stage_id
        WITH NO DATA;

REFRESH MATERIALIZED VIEW customer_full_info;

SELECT * FROM customer_full_info;
rollback;
commit;