/* Task 1.2.1
Создать бд, создать таблицы, добавить связи между таблицами, заполнить таблицу данными
(их нужно сгенерировать в большом количестве - для этого можно использовать последовательности, собственные или встроенные функции - никаких внешних генераторов).
 */

begin;
rollback;

create table if not exists street (
street_id serial primary key not null,
street_name varchar(255) not null
);

create table if not exists city (
city_id serial primary key not null,
city_name varchar(255) not null
);

create table if not exists stage (
stage_id serial primary key not null,
stage_name varchar(255) not null
);

create table if not exists address (
address_id serial primary key not null,
street_street_id int references street(street_id) not null ,
city_city_id int references city(city_id) not null,
stage_stage_id int references stage(stage_id) not null
);

create table if not exists car_brand (
    brand_id serial primary key not null,
    brand_name varchar(20) not null,
    brand_full_name varchar(255)
);

create table if not exists car_model (
  model_id serial primary key not null,
  model_name varchar(255) not null,
  car_brand_brand_id int references car_brand(brand_id)
);

create table if not exists cars (
    car_id serial primary key not null,
    car_plate varchar(10) not null,
    car_brand_brand_id int references car_brand(brand_id),
    car_model_model_id int references car_model(model_id)
);

create table if not exists phone_code (
    code_id serial primary key not null,
    code smallint not null
    -- code like 380 for ukraine
);

create table if not exists phone (
    phone_id serial primary key not null,
    phone_code_code_id serial references phone_code(code_id),
    phone_number int not null
);

create table if not exists customer (
    user_id serial primary key not null,
    first_name varchar(25) not null,
    second_name varchar(25) not null,
    phone_phone_id int references phone(phone_id),
    cars_car_id int references cars(car_id),
    address_address_id int references address(address_id)
);

create table if not exists branch (
    branch_id serial primary key not null,
    phone_phone_id int references phone(phone_id),
    address_address_id int references address(address_id)
);

create table if not exists products (
    product_id serial primary key not null,
    cars_car_id int references cars(car_id),
    branch_branch_id int references branch(branch_id)
);

create table if not exists orders (
    order_id serial primary key not null,
    customer_user_id int references customer(user_id) not null ,
    products_product_id int references products(product_id) not null ,
    price money not null,
    renting_period timestamp(2) not null ,
    renting_day timestamp(2) not null
);

commit;

begin;

CREATE OR REPLACE FUNCTION address_generator()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var_r record;
    BEGIN
        for var_r in
            select generate_series(1,500) as id
        loop
            insert into street (street_name)
            values (('street ' || var_r.id)::text);
            insert into city (city_name)
            values (('city ' || var_r.id)::text);
            insert into stage (stage_name)
            values (('stage ' || var_r.id)::text);
        END loop;
        RETURN var_r;
    END;
$$;

select address_generator();
select * from street;
rollback;
commit;
/*
ALTER SEQUENCE street_street_id_seq RESTART WITH 1;
ALTER SEQUENCE city_city_id_seq RESTART WITH 1;
ALTER SEQUENCE address_address_id_seq RESTART WITH 1;
ALTER SEQUENCE stage_stage_id_seq RESTART WITH 1;
*/
select * from address;

begin;
-- crutch
insert into address (street_street_id, city_city_id, stage_stage_id)
    select s.street_id, c.city_id, st.stage_id
    from street as s
    join city c on c.city_id=s.street_id
    join stage st on st.stage_id=s.street_id;

select * from address;
commit;

begin;
CREATE OR REPLACE FUNCTION cars_generator()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var_r record;
    BEGIN
        for var_r in
            select generate_series(1, 1000) as id
        loop
            insert into car_brand (brand_name, brand_full_name)
            values (('cb ' || var_r.id)::text, ('brand ' || var_r.id)::text);
            insert into car_model (model_name)
            values (('model ' || var_r.id)::text);
        END loop;
        RETURN var_r;
    END;
$$;
select cars_generator();

savepoint create_cars_generator;

update car_model c
set car_brand_brand_id = (select brand_id
                        from car_brand
                        where brand_id=c.model_id)
where (car_brand_brand_id::text = '') IS NOT FALSE;

ROLLBACK to savepoint create_cars_generator;

savepoint create_cars_model;

ROLLBACK to savepoint create_cars_model;

-- ALTER SEQUENCE car_brand_brand_id_seq RESTART WITH 1;
-- ALTER SEQUENCE car_model_model_id_seq RESTART WITH 1;

ROLLBACK;

select substr(md5(random()::text), 0, 10);
commit;

begin;

CREATE OR REPLACE FUNCTION cars()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var record;
    BEGIN
        for var in
            select generate_series(1, 500) as id
        loop
            insert into cars (car_plate, car_brand_brand_id, car_model_model_id)
            values (substr(md5(random()::text), 0, 10),
                    var.id, var.id
                    );
        END loop;
        RETURN var;
    END;
$$;
select cars();
select * from cars where car_id=1001;
ALTER SEQUENCE cars_car_id_seq RESTART WITH 1001;
commit;



begin;
--phone_code
CREATE OR REPLACE FUNCTION phone_code_fu()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var record;
    BEGIN
        for var in
            select generate_series(1, 1000) as id
        loop
            insert into phone_code (code)
            values (floor(random()*1000));
        END loop;
        RETURN var;
    END;
$$;
select phone_code_fu();
commit;

begin;
--phone

CREATE OR REPLACE FUNCTION phone_fu()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var record;
    BEGIN
        for var in
            select generate_series(1, 1000) as id
        loop
            insert into phone (phone_code_code_id, phone_number)
            values (var.id, floor(random()*1000000000));
        END loop;
        RETURN var;
    END;
$$;
select phone_fu();
commit;

--customer
begin;
CREATE OR REPLACE FUNCTION customer_fu()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var record;
    BEGIN
        for var in
            select generate_series(1, 500) as id
        loop
            insert into customer (first_name, second_name, phone_phone_id, cars_car_id, address_address_id)
            values ('name ' || var.id, 'second_name ' || var.id, var.id, var.id, var.id);
        END loop;
        RETURN var;
    END;
$$;
select customer_fu();
select * from customer;
ALTER SEQUENCE customer_user_id_seq RESTART WITH 1;
rollback;
commit;

--branch
begin;
CREATE OR REPLACE FUNCTION branch_fu()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var record;
    BEGIN
        for var in
            select generate_series(1, 500) as id
        loop
            insert into branch (phone_phone_id, address_address_id)
            values (500+var.id, var.id);
        END loop;
        RETURN var;
    END;
$$;
select branch_fu();
select * from branch;
ALTER SEQUENCE branch_branch_id_seq RESTART WITH 1;
rollback;
commit;

--products
begin;
CREATE OR REPLACE FUNCTION products_fu()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var record;
    BEGIN
        for var in
            select generate_series(1, 500) as id
        loop
            insert into products (cars_car_id, branch_branch_id)
            values (var.id, var.id);
        END loop;
        RETURN var;
    END;
$$;
select products_fu();
select * from products;
ALTER SEQUENCE products_product_id_seq RESTART WITH 1;
rollback;
commit;


--orders
begin;
CREATE OR REPLACE FUNCTION orders_fu()
    returns VARCHAR
    LANGUAGE plpgsql
as $$
    DECLARE
        var record;
    BEGIN
        for var in
            select generate_series(1, 500) as id
        loop
            insert into orders (customer_user_id, products_product_id, price, renting_period, renting_day)
            values (var.id, var.id, floor(random()*10000)::int::money,
                    (format('2021-%s-%s', floor(random()*10+1), floor(random()*10+1)))::timestamp,
                    (format('2021-%s-%s', floor(random()*10+1), floor(random()*10+1)))::timestamp);
        END loop;
        RETURN var;
    END;
$$;
select orders_fu();
select * from orders where order_id > 2000;
ALTER SEQUENCE orders_order_id_seq RESTART WITH 1301;
rollback;


commit;

select (format('2021-%s-%s', floor(random()*10), floor(random()*10)))::timestamp(2);

select floor(random()*10000);