
-- create database
CREATE DATABASE academy;

-- create table
CREATE TABLE person (Id SERIAL PRIMARY KEY,name varchar(255) NOT NULL,age int NOT NULL,student boolean);

-- insert entries
INSERT INTO person (name, age, student) VALUES ('aino', 29, True);

-- list entries from table
SELECT * FROM person;
SELECT Id AS Identifier, name FROM person;
SELECT Id, name FROM person;

-- order entries
SELECT * FROM person ORDER BY name ASC;
SELECT * FROM person ORDER BY name DESC;

-- count rows
SELECT count(*) FROM person;

-- ages sum
SELECT SUM (age) AS ages FROM person;

-- average age
SELECT AVG (age) AS average FROM person;

-- updating a row
UPDATE person SET age = 29 WHERE name = 'aino';
UPDATE person SET student = False;

-- delete row
DELETE FROM person WHERE id = 1;

-- delete table
DROP TABLE person;

-- harjoitus 6 ->
CREATE TABLE certificates
    (
        Id          SERIAL PRIMARY KEY,
        name        varchar(255) NOT NULL,
        person_id   int,
        CONSTRAINT  fk_person
            FOREIGN KEY(person_id)
                REFERENCES person(id)
    );

INSERT INTO person (Id, name, age, student) VALUES (1, 'aino', 29, True);

-- certificates table
INSERT INTO certificates (name, person_id) VALUES ('AZ-104', 1);
SELECT * FROM certificates;
INSERT INTO certificates (name, person_id) VALUES ('Scrum Master', 2);
INSERT INTO certificates (name, person_id) VALUES ('Scrum Master', 3);
INSERT INTO certificates (name, person_id) VALUES ('AZ-104', 4);
INSERT INTO certificates (name, person_id) VALUES ('AZ-104', 5);
INSERT INTO certificates (name, person_id) VALUES ('AWS', 6);

SELECT * FROM certificates WHERE name = 'Scrum Master';
SELECT * FROM certificates WHERE name = 'AZ-104';

-- limit results
SELECT * FROM city LIMIT 10;

-- filter results
SELECT * FROM city WHERE country_code = 'FIN';
SELECT count (*) FROM city WHERE country_code = 'USA';
SELECT SUM (population) FROM city WHERE country_code = 'USA';
SELECT * FROM city WHERE population BETWEEN 1000000 and 2000000 LIMIT 15;
SELECT SUM (population) FROM city WHERE country_code = 'USA';
SELECT district, SUM (population) FROM city WHERE country_code = 'USA' GROUP BY district;
SELECT name, lifeexpectancy FROM country WHERE lifeexpectancy IS NOT NULL ORDER BY lifeexpectancy DESC LIMIT 1;
SELECT country_code, SUM(population) FROM city GROUP BY country_code ORDER BY SUM(population) DESC LIMIT 3;
SELECT name, population FROM country ORDER BY population DESC LIMIT 3;
SELECT country_code, SUM(population) FROM city GROUP BY country_code ORDER BY SUM(population) DESC LIMIT 3; SELECT name, population FROM country ORDER BY population DESC LIMIT 3;

-- join
SELECT country.name, country.capital FROM country INNER JOIN city ON country.code = city.country_code WHERE country.code = 'ESP';
SELECT continent FROM country
SELECT country.name, city.name FROM country INNER JOIN city ON country.capital = city.id WHERE continent = 'Europe';
SELECT country.name, city.name AS capital FROM country INNER JOIN city ON country.capital = city.id WHERE country.code = 'ESP';
SELECT country.name, city.name AS capital FROM country INNER JOIN city ON country.capital = city.id;
SELECT country.name, country_language.language FROM country INNER JOIN country_language ON country.code = country_language.country_code WHERE country.region = 'Southeast Asia';

-- subqueries
SELECT name, population FROM city WHERE population >
    (SELECT population FROM country WHERE name = 'Finland');
SELECT country.name, country_language.language FROM country INNER JOIN country_language ON country.code = country_language.country_code WHERE country.region = 'Southeast Asia';
