# -----------------------------
# Online Learning Management System database setup and table creation

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from faker import Faker

# Initialize Faker
fake = Faker()

# Create a SQLite database
engine = create_engine(
    'sqlite:///online_learning_management_system.db', echo=True)

Base = declarative_base()

# Define tables

# Define a Course table


class Course(Base):
    __tablename__ = 'Courses'
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String, nullable=False)
    description = Column(String)

    assignments = relationship("Assignment", back_populates="course")
    enrollments = relationship("Enrollment", back_populates="course")

# Define an Instructor table


class Instructor(Base):
    __tablename__ = 'Instructors'
    instructor_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

# Define a Student table


class Student(Base):
    __tablename__ = 'Students'
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    submissions = relationship("Submission", back_populates="student")
    enrollments = relationship("Enrollment", back_populates="student")

# Define an Enrollment table


class Enrollment(Base):
    __tablename__ = 'Enrollments'
    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('Students.student_id'))
    course_id = Column(Integer, ForeignKey('Courses.course_id'))

    # Define a relationship between Enrollment and Student
    student = relationship("Student", back_populates="enrollments")

    # Define a relationship between Enrollment and Course
    course = relationship("Course", back_populates="enrollments")

# Define an Assignment table


class Assignment(Base):
    __tablename__ = 'Assignments'
    assignment_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('Courses.course_id'))
    title = Column(String, nullable=False)
    due_date = Column(Date)

    # Define a relationship between Assignment and Course
    course = relationship("Course", back_populates="assignments")

    # Define a relationship between Assignment and Submission
    submissions = relationship("Submission", back_populates="assignment")

# Define a Submission table


class Submission(Base):
    __tablename__ = 'Submissions'
    submission_id = Column(Integer, primary_key=True, autoincrement=True)
    assignment_id = Column(Integer, ForeignKey('Assignments.assignment_id'))
    student_id = Column(Integer, ForeignKey('Students.student_id'))
    submission_date = Column(Date)

    # Define a relationship between Submission and Assignment
    assignment = relationship("Assignment", back_populates="submissions")


# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert mock data
instructor = Instructor(name=fake.name(), email=fake.email())
session.add(instructor)

student = Student(name=fake.name(), email=fake.email())
session.add(student)

course = Course(course_name=fake.company(), description=fake.catch_phrase())
session.add(course)

session.commit()

# Fetch the inserted IDs
inserted_course = session.query(Course).first()
inserted_student = session.query(Student).first()

assignment = Assignment(course_id=inserted_course.course_id,
                        title=fake.bs(), due_date=fake.date())
session.add(assignment)

submission = Submission(assignment_id=1, student_id=inserted_student.student_id,
                        submission_date=fake.date(), grade=fake.random_int(min=0, max=100))
session.add(submission)

enrollment = Enrollment(student_id=inserted_student.student_id,
                        course_id=inserted_course.course_id)
session.add(enrollment)

# Commit the transaction
session.commit()
