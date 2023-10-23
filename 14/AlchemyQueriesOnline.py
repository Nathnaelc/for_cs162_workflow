from sqlalchemy import create_engine, sessionmaker
from learning_management_models import Course, Student, Enrollment

# Initialize database connection
learning_engine = create_engine(
    'sqlite:///online_learning_management_system.db')

# Create session
LearningSession = sessionmaker(bind=learning_engine)
learning_session = LearningSession()

# Query for Learning Management System
print("\nLearning Management System Queries:")

# Get all courses
courses = learning_session.query(Course).all()
print("Courses:")
for course in courses:
    print(course.course_name, course.description)

# Get all students enrolled in a specific course (Course ID 1)
students_in_course = learning_session.query(Student).join(
    Enrollment).filter(Enrollment.course_id == 1).all()
print("Students in Course ID 1:")
for student in students_in_course:
    print(student.name, student.email)
