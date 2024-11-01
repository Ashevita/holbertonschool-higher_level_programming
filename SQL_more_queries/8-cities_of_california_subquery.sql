-- Script to list all cities in California
SELECT cities.name
FROM cities
WHERE cities.state_id = (
-- Subquery to get the id of the state "California"
SELECT id FROM states WHERE name = 'California'
)
ORDER BY cities.id ASC;
