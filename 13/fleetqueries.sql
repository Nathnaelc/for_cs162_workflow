-- Which cars are currently available for rent?
SELECT model, make, year FROM Cars WHERE status = 'available';

-- Who are the customers that have rented cars this month?
SELECT DISTINCT c.name FROM Customers c
JOIN Rentals r ON c.id = r.customer_id
WHERE strftime('%Y-%m', r.start_date) = strftime('%Y-%m', 'now');

-- What is the total maintenance cost for each car this year?
SELECT c.model, SUM(m.cost) as Total_Maintenance_Cost
FROM Cars c
JOIN Maintenance m ON c.id = m.car_id
WHERE strftime('%Y', m.start_date) = strftime('%Y', 'now')
GROUP BY c.id;

-- How many times has each car been rented?
SELECT c.model, COUNT(r.id) as Rental_Count
FROM Cars c
JOIN Rentals r ON c.id = r.car_id
GROUP BY c.id;

-- What is the average rental duration for each car?
SELECT c.model, AVG(julianday(r.end_date) - julianday(r.start_date)) as Avg_Rental_Duration
FROM Cars c
JOIN Rentals r ON c.id = r.car_id
GROUP BY c.id;
