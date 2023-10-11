### Fitness Class Booking and Attendance Tracking

- **Class** table: Stores information about fitness classes.
- **Student** table: Stores information about students.
- **Booking** table: Records class bookings made by students.
- **Attendance** table: Tracks attendance in classes.

Entity-Relationship Diagram

[![The fitness class app](https://mermaid.ink/img/pako:eNqNUrtuwzAM_BWBc_ID2trUKDykQ-OhgxdGYhPBthRI9BA4_vfIlhHIDQJ0EXhH4vg4DaCcJpBA_sPgyWNXWyF2LYYghikUwmhRflXFZ_GdsMWORFX8VEvaBva9Yuczks1UU-6LBBVeUBm-5kLj9By412T5n62oQ9M-8Czw7lxj7OmVQEj65R9aTfutyVntjZmsRqvoleAx9Suf-iD3YT1aOuLttt264TGnFGcM-eZP-alDyFdbKrLZpGCPqgmwgY58PIqOBs4D18Bn6qgGGUONvqmhtmOsw57d4WoVyGgWbaC_aGRaLF-ThTbRTJC_2IZI0gz36ZfMn2W8A2jctMM?type=png)](https://mermaid.live/edit#pako:eNqNUrtuwzAM_BWBc_ID2trUKDykQ-OhgxdGYhPBthRI9BA4_vfIlhHIDQJ0EXhH4vg4DaCcJpBA_sPgyWNXWyF2LYYghikUwmhRflXFZ_GdsMWORFX8VEvaBva9Yuczks1UU-6LBBVeUBm-5kLj9By412T5n62oQ9M-8Czw7lxj7OmVQEj65R9aTfutyVntjZmsRqvoleAx9Suf-iD3YT1aOuLttt264TGnFGcM-eZP-alDyFdbKrLZpGCPqgmwgY58PIqOBs4D18Bn6qgGGUONvqmhtmOsw57d4WoVyGgWbaC_aGRaLF-ThTbRTJC_2IZI0gz36ZfMn2W8A2jctMM)

This application is designed to manage fitness class bookings and track attendance. It allows users to browse available fitness classes, book them, and keeps records of attendance. Instructors can also use it to monitor and manage class participation.

Question 1: What are the names and times of all fitness classes?
-- Answer to Question 1:
SELECT name, time
FROM Class;

output:
| name | time |
| --------- | ------- |
| Yoga | 09:00AM |
| Pilates | 10:30AM |
| Zumba | 12:00PM |

Question 2: How many students have booked classes?

-- Answer to Question 2:
SELECT COUNT(\*) as total_students_booked
FROM Booking;

output:
| total_students_booked |
| ---------------------- |
| 4 |

Question 3: List the names of students who attended the "Yoga" class.

-- Answer to Question 3:
SELECT S.name
FROM Student S
INNER JOIN Booking B ON S.id = B.studentId
INNER JOIN Class C ON B.classId = C.id
WHERE C.name = 'Yoga';

| name       |
| ---------- |
| John Doe   |
| Jane Smith |
