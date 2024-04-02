-- create user and database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_06_2'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_06_2'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
