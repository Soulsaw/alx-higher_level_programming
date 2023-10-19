-- Create a force_name table if doesn't exists
-- Create a database hbtn_0d_usa if not exist 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use this database
use hbtn_0d_usa;
-- Create a table if not exists
CREATE TABLE IF NOT EXISTS states
(
    id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(256) NOT NULL
);
