-- script for create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utilise la base de données hbtn_0d_usa
USE hbtn_0d_usa;

-- script for create table
CREATE TABLE IF NOT EXISTS states (
		id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
		name VARCHAR(256) NOT NULL
);
