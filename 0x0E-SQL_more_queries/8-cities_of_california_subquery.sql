-- List of all the cities of the california
SELECT cities.id,cities.name FROM cities
WHERE cities.state_id IN (
    SELECT states.id FROM states
    WHERE states.name = "California"
    )
ORDER BY cities.id ASC;
