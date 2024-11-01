-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use database
USE hbtn_0d_usa;

-- create table if not exists
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
