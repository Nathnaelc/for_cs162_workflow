-- How many tickets are currently open?
SELECT COUNT(*) FROM Tickets WHERE status = 'open';

-- Which agents have been assigned the most tickets?
SELECT agent_id, COUNT(*) as ticket_count
FROM Ticket_Assignments
GROUP BY agent_id
ORDER BY ticket_count DESC
LIMIT 5;

-- What are the most common types of issues?
SELECT issue_type, COUNT(*) as issue_count
FROM Tickets
GROUP BY issue_type
ORDER BY issue_count DESC;

-- How many tickets were closed this month?
SELECT COUNT(*) 
FROM Tickets
WHERE status = 'closed' AND strftime('%Y-%m', closed_at) = strftime('%Y-%m', 'now');

-- What is the average time taken to close a ticket?
SELECT AVG(JULIANDAY(closed_at) - JULIANDAY(created_at)) as avg_days
FROM Tickets
WHERE status = 'closed';
