--- This script print all row only the name and score
--- description of the table second_table
SELECT `score`,`name`
    FROM `second_table`
WHERE `name` = 'John'
ORDER BY `score` DESC;
