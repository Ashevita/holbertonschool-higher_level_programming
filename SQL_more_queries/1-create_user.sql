-- script for create an user with password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- script for atribute all privilege
GRANT ALL PRIVILEGES on *.* to 'user_0d_1'@'localhost';
