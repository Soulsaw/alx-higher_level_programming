-- This script create an inexisting user
-- This query permit to create an inexisting user_0d_1 with the password user_0d_1_pwd
CREATE USER  IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- This query permit to gant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
