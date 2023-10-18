--- This script print all row only the name and score
--- description of the table second_table
SELECT `score`,`name`
    FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
