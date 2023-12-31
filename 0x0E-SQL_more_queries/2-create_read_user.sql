-- Create an user and database and give the select permission on the database to the user
-- This query permit to create a non existing database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- This query permit to create a non existing user_0d_2 with the password user_0d_2_pwd
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- TH=his query permit to grant select privileges on the database hbtn_0d_2 to the user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
