-- This script permit to create the first_table
-- with the in and name like its attributes
CREATE TABLE IF NOT EXISTS `second_table`
(
	`id` INT,
	`name` VARCHAR(256),
	`score` INT
);
-- inserting data in the second_table
INSERT INTO `second_table`(`id`,`name`,`score`)
VALUES
(1,'John',10),
(2,'Alex',3),
(3,'Bob',14),
(4,'Gorge',8);
