-- This script print all row only the name and score
-- description of the table second_table
SELECT score,name
    FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
