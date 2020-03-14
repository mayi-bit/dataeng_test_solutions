
BEGIN;

SET client_encoding = 'LATIN1';

CREATE TABLE customer_details(
 	customer_id int primary key, 
  	customer_name varchar, 
  	customer_phone_number int);


CREATE TABLE car_details (
	car_serial_number bigint primary key, 
	car_model varchar, 
	car_model_variant varchar, 
	car_price int, 
	car_wight int, 
	car_engine_cc int, 
	car_condition varchar, 
	car_manufacturer varchar);


CREATE TABLE transactions (
	timestamp timestamp,
	customer_id int, 
	car_serial_number bigint, 
	salesperson varchar, 
	primary key (car_serial_number, salesperson));


