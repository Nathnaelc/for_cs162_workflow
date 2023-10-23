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






-- Transaction for adding a new course and enrolling a student
BEGIN TRANSACTION;
    INSERT INTO Courses (course_name, description) VALUES ('New Course', 'This is a new course.');
    INSERT INTO Enrollments (student_id, course_id) VALUES (1, LAST_INSERT_ROWID());
COMMIT;

-- Explanation: This transaction ensures that when a new course is added, a student is also enrolled in it. If either operation fails, the transaction will be rolled back.

-- Transaction for adding a new assignment and a submission
BEGIN TRANSACTION;
    INSERT INTO Assignments (course_id, title, due_date) VALUES (1, 'New Assignment', '2023-12-31');
    INSERT INTO Submissions (assignment_id, student_id, submission_date, grade) VALUES (LAST_INSERT_ROWID(), 1, '2023-11-11', 90);
COMMIT;
-- Explanation: This transaction ensures that when a new assignment is added to a course, a submission is also created for it. If either operation fails, the transaction will be rolled back.
