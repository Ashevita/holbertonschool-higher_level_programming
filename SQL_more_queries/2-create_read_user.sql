-- Write a script that creates the database hbtn_0c_0 in your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- script for create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- script for atribute SELECT privilege
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
