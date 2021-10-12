CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday)
VALUES (1, 'Ororo Munroe', '1940-05-30');

INSERT INTO friends (id, name, birthday)
VALUES (2, 'John Doe', '1980-01-01');

INSERT INTO friends (id, name, birthday)
VALUES (3, 'Jane Doe', '1970-02-02');

UPDATE friends
SET name = 'Storm'
WHERE id = 1;

ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;

UPDATE friends
SET email = 'johnd@codecademy.com'
WHERE id = 2;

UPDATE friends
SET email = 'janed@codecademy.com'
WHERE id = 3;

DELETE FROM friends
WHERE id = 1;

SELECT *
FROM friends;

-----------------------------------

SELECT *
FROM nomnom;

SELECT DISTINCT neighborhood
FROM nomnom;

SELECT DISTINCT cuisine
FROM nomnom;

SELECT *
FROM nomnom
WHERE cuisine = 'Chinese';

SELECT *
FROM nomnom
WHERE review >= 4;

SELECT *
FROM nomnom
WHERE cuisine = 'Italian'
   AND price = '$$$';

SELECT *
FROM nomnom
WHERE cuisine = 'Italian'
   AND price LIKE '%$$$%';

SELECT *
FROM nomnom
WHERE name LIKE '%meatball%';

SELECT *
FROM nomnom
WHERE neighborhood = 'Midtown'
   OR neighborhood = 'Downtown'
   OR neighborhood = 'Chinatown';

SELECT *
FROM nomnom
WHERE health IS NULL;

SELECT *
FROM nomnom
ORDER BY review DESC;

SELECT *
FROM nomnom
ORDER BY review DESC
LIMIT 10;

SELECT name,
 CASE
  WHEN review > 4.5 THEN 'Extraordinary'
  WHEN review > 4 THEN 'Excellent'
  WHEN review > 3 THEN 'Good'
  WHEN review > 2 THEN 'Fair'
  ELSE 'Poor'
 END AS 'Review'
FROM nomnom;

#-----------------------------------------#

SELECT *
FROM startups;

SELECT COUNT(*)
FROM startups;

SELECT SUM(valuation)
FROM startups;

SELECT MAX(raised)
FROM startups;

SELECT MAX(raised)
FROM startups
WHERE stage = 'Seed';

SELECT MIN(founded)
FROM startups;

SELECT AVG(valuation)
FROM startups;

SELECT category, AVG(valuation)
FROM startups
GROUP BY category;

SELECT category, ROUND(AVG(valuation), 2)
FROM startups
GROUP BY category;

SELECT category, ROUND(AVG(valuation), 2)
FROM startups
GROUP BY 1
ORDER BY 2 DESC;

SELECT category, COUNT(*)
FROM startups
GROUP BY category;

SELECT category, COUNT(*)
FROM startups
GROUP BY category
HAVING COUNT(*) > 3;

SELECT category, COUNT(*)
FROM startups
GROUP BY category
HAVING COUNT(*) > 3
ORDER BY 2 DESC;

SELECT location, AVG(employees)
FROM startups
GROUP BY location;

SELECT location, AVG(employees)
FROM startups
GROUP BY location
HAVING AVG(employees) > 500;

#-------------------------------------------#

SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

SELECT SUM(score)
FROM hacker_news;

SELECT user, SUM(score)
FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200
ORDER BY 2 DESC;

SELECT (517 + 309 + 304 + 282) / 6366.0;

SELECT user,
   COUNT(*)
FROM hacker_news
WHERE url LIKE '%watch?v=dQw4w9WgXcQ%'
GROUP BY user
ORDER BY COUNT(*) DESC;

SELECT user,
   COUNT(*)
FROM hacker_news
WHERE url LIKE '%watch?v=dQw4w9WgXcQ%'
GROUP BY 1
ORDER BY 2 DESC;

SELECT CASE
   WHEN url LIKE '%github.com%' THEN 'GitHub'
   WHEN url LIKE '%medium.com%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
  END AS 'Source'
FROM hacker_news;

SELECT CASE
   WHEN url LIKE '%github.com%' THEN 'GitHub'
   WHEN url LIKE '%medium.com%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
  END AS 'Source',
  COUNT(*)
FROM hacker_news
GROUP BY 1;

SELECT timestamp
FROM hacker_news
LIMIT 10;

SELECT timestamp,
   strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;

SELECT strftime('%H', timestamp), 
   AVG(score),
   COUNT(*)
FROM hacker_news
GROUP BY 1
ORDER BY 1;

SELECT strftime('%H', timestamp) AS 'Hour', 
   ROUND(AVG(score), 1) AS 'Average Score', 
   COUNT(*) AS 'Number of Stories'
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER BY 1;

#--------------------------------------------#

SELECT * FROM trips;
SELECT * FROM riders;
SELECT * FROM cars;

SELECT riders.first,
   riders.last,
   cars.model
FROM riders, cars;

SELECT *
FROM trips
LEFT JOIN riders 
  ON trips.rider_id = riders.id;

SELECT trips.date, 
   trips.pickup, 
   trips.dropoff, 
   trips.type, 
   trips.cost,
   riders.first, 
   riders.last,
   riders.username
FROM trips
LEFT JOIN riders 
  ON trips.rider_id = riders.id;

SELECT *
FROM trips
JOIN cars
  ON trips.car_id = cars.id;

SELECT *
FROM riders
UNION
SELECT *
FROM riders2;

SELECT AVG(cost)
FROM trips;

SELECT *
FROM riders
WHERE total_trips < 500;

SELECT *
FROM riders
WHERE total_trips < 500
UNION
SELECT *
FROM riders2
WHERE total_trips < 500;

SELECT COUNT(*)
FROM cars
WHERE status = 'active';

SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;