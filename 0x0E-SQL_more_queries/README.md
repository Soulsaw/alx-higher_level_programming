# 0x0E. SQL - More queries
## 0. My privileges!
[Task 0](./0-privileges.sql) Write a script that lists all privileges of the MySQL users
## 1. Root user
[Task 1](./1-create_user.sql) Write a script that creates the MySQL server user user_0d_1.
## 2. Read user
[Task 2](./2-create_read_user.sql) Write a script that creates the database hbtn_0d_2 and the user user_0d_2
## 3. Always a name
[Task 3](./3-force_name.sql) Write a script that creates the table force_name on your MySQL server.
* **Description of the table force_name**
1. ```id``` INT
2. ```name``` VARCHAR(256)
## 4. ID can't be null
[Task 4](./4-never_empty.sql) Write a script that creates the table id_not_null on your MySQL server.
* **Description of the table id_not_null**
1. ```id``` INT DEFAULT 1
2. ```name``` VARCHAR(256)
## 5. Unique ID
[Task 5](./5-unique_id.sql) Write a script that creates the table unique_id on your MySQL server.
* **Description of the table unique_id**
1. ```id``` INT DEFAULT 1 UNIQUE
2. ```name``` VARCHAR(256)
## 6. States table
[Task 6](./6-states.sql) Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
* Create the database if not exists
* *Description of the table states*
1. ```id``` INT DEFAULT 1 UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY
2. ```name``` VARCHAR(256) NOT NULL
## 7. Cities table
[Task 7](./7-cities.sql) Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
* Create the database if not exists
* *Description of the table cities*
1. ```id``` INT DEFAULT 1 UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY
2. ```state_id``` INT NOT NULL FOREIGN KEY
3. ```name``` VARCHAR(256) NOT NULL
## 8. Cities of California
[Task 8](./8-cities_of_california_subquery.sql) Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
* The states table contains only one record where name = California (but the id can be different, as per the example)
* Results must be sorted in ascending order by cities.id
## 9. Cities by States
[Task 9](./9-cities_by_state_join.sql) Write a script that lists all cities contained in the database hbtn_0d_usa
* Each record should display: ```cities.id - cities.name - states.name```
* Results must be sorted in ascending order by cities.id
## 10. Genre ID by show
[Task 10](./10-genre_id_by_show.sql) Import the database dump from hbtn_0d_tvshows to your MySQL server:[Download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

