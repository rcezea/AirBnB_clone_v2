-- create a database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a new user hbnb_test and set password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_test_pwd';
-- grant all database privileges to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant select privilege on performance_schema to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;