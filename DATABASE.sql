CREATE USER sber3 WITH PASSWORD 'sber3';
ALTER ROLE sber3 SET client_encoding TO 'utf8';
ALTER ROLE sber3 SET default_transaction_isolation TO 'read committed';
ALTER ROLE sber3 SET timezone TO 'UTC';
ALTER USER sber3 CREATEDB;


CREATE DATABASE sber3;
GRANT ALL PRIVILEGES ON DATABASE sber3 TO sber3;