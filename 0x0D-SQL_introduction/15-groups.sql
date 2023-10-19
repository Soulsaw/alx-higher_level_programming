--- This script print all row from
--- description of the table first_table
SELECT `score`, COUNT(`score`) as 'number'
    FROM `second_table`
GROUP BY `score`
ORDER BY `score` DESC;
