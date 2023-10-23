# Create a fleet management app using SQLAlchemy
# import the required libraries
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from faker import Faker

# Initialize Faker
fake = Faker()

# Create a SQLite database
engine = create_engine('sqlite:///fleet_management.db', echo=True)

Base = declarative_base()

# Define tables

# Define a Car table


class Car(Base):
    __tablename__ = 'Cars'
    car_id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String, nullable=False)
    make = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    status = Column(String, nullable=False)

    rentals = relationship("Rental", back_populates="car")
    maintenances = relationship("Maintenance", back_populates="car")

# Define a Customer table


class Customer(Base):
    __tablename__ = 'Customers'
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False)

    rentals = relationship("Rental", back_populates="customer")

# Define a Rental table


class Rental(Base):
    __tablename__ = 'Rentals'
    rental_id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('Cars.car_id'))
    customer_id = Column(Integer, ForeignKey('Customers.customer_id'))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_price = Column(Float, nullable=False)

    car = relationship("Car", back_populates="rentals")
    customer = relationship("Customer", back_populates="rentals")

# Define a Maintenance table


class Maintenance(Base):
    __tablename__ = 'Maintenance'
    maintenance_id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('Cars.car_id'))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    cost = Column(Float, nullable=False)

    car = relationship("Car", back_populates="maintenances")


# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert mock data
for _ in range(5):
    car = Car(model=fake.company(), make=fake.company_suffix(),
              year=fake.year(), status='Available')
    session.add(car)

    customer = Customer(name=fake.name(), email=fake.email(),
                        phone=fake.phone_number())
    session.add(customer)

    rental = Rental(car_id=1, customer_id=1, start_date=fake.date(
    ), end_date=fake.date(), total_price=fake.random_number(digits=4))
    session.add(rental)

    maintenance = Maintenance(car_id=1, start_date=fake.date(
    ), end_date=fake.date(), cost=fake.random_number(digits=3))
    session.add(maintenance)

# Commit the transaction
session.commit()

# Nathe
all_cars = session.query(Car).all()
for car in all_cars:
    print(car.car_id, car.model, car.make, car.year, car.status)

all_customers = session.query(Customer).all()
for customer in all_customers:
    print(customer.customer_id, customer.name, customer.email, customer.phone)

    all_rentals = session.query(Rental).all()
for rental in all_rentals:
    print(rental.rental_id, rental.car_id, rental.customer_id,
          rental.start_date, rental.end_date, rental.total_price)

    all_maintenance = session.query(Maintenance).all()
for maintenance in all_maintenance:
    print(maintenance.maintenance_id, maintenance.car_id,
          maintenance.start_date, maintenance.end_date, maintenance.cost)

    available_cars = session.query(Car).filter_by(status='Available').all()
for car in available_cars:
    print(car.car_id, car.model, car.make, car.year, car.status)

    customer_rentals = session.query(Rental).filter_by(customer_id=1).all()
for rental in customer_rentals:
    print(rental.rental_id, rental.car_id, rental.customer_id,
          rental.start_date, rental.end_date, rental.total_price)
