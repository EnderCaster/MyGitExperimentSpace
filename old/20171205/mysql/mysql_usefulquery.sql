create database TEST;
use TEST;
CREATE TABLE shop (
     article INT(4) UNSIGNED ZEROFILL DEFAULT '0000' NOT NULL,
     dealer  CHAR(20)                 DEFAULT ''     NOT NULL,
     price   DOUBLE(16,2)             DEFAULT '0.00' NOT NULL,
     PRIMARY KEY(article, dealer));
INSERT INTO shop VALUES
     (1,'A',3.45),(1,'B',3.99),(2,'A',10.99),(3,'B',1.45),
     (3,'C',1.69),(3,'D',1.25),(4,'D',19.95);
SELECT * FROM shop;
SELECT MAX(article) as article FROM shop;
SELECT article,dealer,price
     FROM shop
     WHERE price=(SELECT MAX(price) FROM shop);
SELECT article,dealer,price
     FROM shop
     ORDER BY price DESC
     LIMIT 1;
SELECT article,MAX(price) AS price
     FROM shop
     GROUP BY article;
SELECT @min_price:=MIN(price),@max_price:=MAX(price) FROM shop;
SELECT * FROM shop WHERE price=@min_price OR price=@max_price;
CREATE TABLE person(
     id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
     name CHAR(60) NOT NULL,
     PRIMARY KEY(id)
);
CREATE TABLE shirt(
     id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
     style ENUM('t-shirt','polo','dress') NOT NULL,
     color ENUM('red','blue','orange','white') NOT NULL,
     owner SMALLINT UNSIGNED NOT NULL REFERENCES person(id),
     PRIMARY KEY (id)
);

INSERT INTO person VALUES (NULL, 'Antonio Paz');

SELECT @last := LAST_INSERT_ID();

INSERT INTO shirt VALUES
     (NULL, 'polo', 'blue', @last),
     (NULL, 'dress', 'white', @last),
     (NULL, 't-shirt', 'blue', @last);

INSERT INTO person VALUES (NULL, 'Lilliana Angelovska');
SELECT @last := LAST_INSERT_ID();
INSERT INTO shirt VALUES
     (NULL, 'dress', 'orange', @last),
     (NULL, 'polo', 'red', @last),
     (NULL, 'dress', 'blue', @last),
     (NULL, 't-shirt', 'white', @last);
CREATE TABLE t1 (year YEAR(4), month INT(2) UNSIGNED ZEROFILL,
    day INT(2) UNSIGNED ZEROFILL);
INSERT INTO t1 VALUES(2000,1,1),(2000,1,20),(2000,1,30),(2000,2,2),
    (2000,2,23),(2000,2,23);
SELECT year,month,BIT_COUNT(BIT_OR(1<<day)) AS days FROM t1
    GROUP BY year,month;
CREATE TABLE animals (
     id MEDIUMINT NOT NULL AUTO_INCREMENT,
     name CHAR(30) NOT NULL,
     PRIMARY KEY (id)
 );

INSERT INTO animals (name) VALUES 
    ('dog'),('cat'),('penguin'),
    ('lax'),('whale'),('ostrich');

SELECT * FROM animals;
