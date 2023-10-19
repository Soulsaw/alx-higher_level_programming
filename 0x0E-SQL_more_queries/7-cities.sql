/* Create a tables cities if doesn't exists */
/* create database hbtn_0d_usa if not exists */
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
/* create the table cities if not exists */
CREATE TABLE IF NOT EXISTS cities
(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id)
);
