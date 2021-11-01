/*
 Задание:
Использовать транзакции для insert, update, delete на 3х таблицах.
Предоставить разнообразные примеры включая возврат к savepoints.
 */

/* CRATE TEST DB FROM OPEN DATA*/
CREATE table imbd_top (
    id SERIAL PRIMARY KEY,
    Title VARCHAR(255),
    film_Year SMALLINT,
    Rated VARCHAR(255),
    Released date,
    Runtime VARCHAR(255),
    Genre VARCHAR(255),
    Director VARCHAR(255),
    Writer VARCHAR(255),
    Actors VARCHAR(255),
    Language VARCHAR(255),
    Country VARCHAR(255),
    Awards VARCHAR(255),
    Ratings_Source VARCHAR(255),
    Ratings_Value VARCHAR(255),
    Metascore SMALLINT,
    imdbRating float,
    imdbVotes int,
    imdbID VARCHAR(255),
    film_Type VARCHAR(255),
    DVD date,
    BoxOffice money,
    Production VARCHAR(255),
    Response VARCHAR(255)
);


CREATE TABLE Imdb (
    id SERIAL PRIMARY KEY,
    imdbid VARCHAR(10),
    title TEXT,
    original_title TEXT,
    year SMALLINT,
    date_published DATE,
    genre VARCHAR(255),
    duration SMALLINT,
    country VARCHAR(255),
    language VARCHAR(50),
    director VARCHAR(255),
    writer VARCHAR(255),
    production_company  VARCHAR(255),
    avg_vote float4,
    votes INT,
    budget money,
    usa_gross_income money,
    worlwide_gross_income money,
    metascore INT,
    reviews_from_users INT,
    reviews_from_critics INT
);

COPY imbd_top(Title,film_Year,Rated,Released,Runtime,
Genre,Director,Writer,Actors,Language,Country,Awards,
Ratings_Source,Ratings_Value,Metascore,imdbRating,imdbVotes,imdbID,film_Type,DVD,
BoxOffice,Production,Response)
FROM '/usr/src/IMDb_ratings.csv'
DELIMITER ',';

COPY imdb(
imdbid,title,original_title,year,
date_published,genre,duration,country,
language,director,writer,production_company,
avg_vote,votes,budget,usa_gross_income,
worlwide_gross_income,metascore,
reviews_from_users,reviews_from_critics)
FROM '/usr/src/IMDb_movies.csv'
DELIMITER ',';



SELECT * FROM Imdb;
SELECT * FROM imbd_top;

SELECT im.title, im.votes, im.year FROM Imdb im
JOIN imbd_top it on im.imdbid = it.imdbID
ORDER BY Im.votes DESC
LIMIT 10;

select * from imbd_top
WHERE Genre LIKE '%Action%'
ORDER BY imdbVotes DESC;

--  Start testing ROLLBACK
BEGIN;
DROP TABLE imbd_top;

SELECT * FROM imbd_top;

ROLLBACK;

SELECT * FROM imbd_top;
-- Fin testing ROLLBACK


-- Start testing TRANSACTION;

/*SET TRANSACTION ISOLATION LEVEL READ COMMITTED;*/

-- Or BEGIN;
START TRANSACTION;

SELECT * FROM Imdb
WHERE (language = '') IS NOT FALSE;


UPDATE Imdb
    SET language = 'None'
WHERE (language = '') IS NOT FALSE;

SAVEPOINT update_lang;

-- Create new table
CREATE TABLE rated_status (
    id SERIAL PRIMARY KEY,
    rated VARCHAR(10)
);

ROLLBACK TO SAVEPOINT update_lang;
-- Insert into new table
INSERT INTO rated_status (rated)
    SELECT DISTINCT rated
    FROM imbd_top;

COMMIT;



BEGIN;

SAVEPOINT new_table_rated;

UPDATE imbd_top it
SET rated = (SELECT id
            FROM rated_status
            WHERE rated_status.rated=it.rated);


ROLLBACK TO SAVEPOINT new_table_rated;

SAVEPOINT update_rated;

-- Chenge type of column rated from VARCHAR to SMALLINT
ALTER TABLE imbd_top ALTER COLUMN rated TYPE SMALLINT USING (rated::SMALLINT);

-- Add FOREIGN KEY column rated
ALTER TABLE imbd_top ADD FOREIGN KEY (rated)
 REFERENCES rated_status(id);

SAVEPOINT add_key;

--DELETE oll old film

DELETE FROM imbd_top
    WHERE film_Year < 1960;

SAVEPOINT delete_old;


ALTER TABLE Imdb DROP COLUMN metascore;

COMMIT;

ROLLBACK TO SAVEPOINT update_rated;

