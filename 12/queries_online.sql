-- 1. What are the courses available?
-- This is fundamental for students to know what courses they can enroll in. It's the starting point for any educational journey on the platform.
SELECT * FROM Courses;


-- SELECT * FROM Courses;
-- 2. Which students are enrolled in a specific course?
--  For instructors, this is vital for tracking attendance, grading, and overall course management.


SELECT s.name 
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.course_id = '2';

output:
-- name
-- Sheri Johnston Holly Meyer
-- Richard Powers


-- SELECT * FROM Assignments;
-- 3. What assignments are due in a specific course?
-- This is important for students to know what they need to do and when they need to do it. It's also important for instructors to know what they need to grade and when they need to grade it.
SELECT title, due_date 
FROM Assignments
WHERE course_id = '2';

-- output:
-- title due_date stay 1973-01-11

-- 4. What is the average grade for a specific assignment?
-- This is important for students to know how they're doing in the course and for instructors to know how the class is doing overall.
SELECT AVG(grade) 
FROM Submissions
WHERE assignment_id = '4';

output:
-- AVG(grade)
-- 75.5






-- DELETE FROM Submissions;
-- DELETE FROM Assignments;
-- DELETE FROM Enrollments;
-- DELETE FROM Students;
-- DELETE FROM Instructors;
-- DELETE FROM Courses;

-- -- Reset auto-increment counters
-- UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='Submissions';
-- UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='Assignments';
-- UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='Enrollments';
-- UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='Students';
-- UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='Instructors';
-- UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='Courses';
