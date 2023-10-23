from sqlalchemy import create_engine, sessionmaker
from fleet_management_models import Car, Customer, Rental

# Initialize database connection
fleet_engine = create_engine('sqlite:///fleet_management.db')

# Create session
FleetSession = sessionmaker(bind=fleet_engine)
fleet_session = FleetSession()

# Query for Fleet Management System
print("Fleet Management System Queries:")

# Get all cars that are available
available_cars = fleet_session.query(Car).filter_by(status='available').all()
print("Available Cars:")
for car in available_cars:
    print(car.model, car.make, car.year)

# Get all customers who have rented a car
customers_rented = fleet_session.query(Customer).join(Rental).distinct().all()
print("Customers who have rented a car:")
for customer in customers_rented:
    print(customer.name, customer.email)
