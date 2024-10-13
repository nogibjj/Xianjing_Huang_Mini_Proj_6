"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD

# Extract
print("Extracting data...")
extract()
print("Extracting data successfully!")

# Transform and load
print("Transforming data...")
load()
print("Transforming data successfully!")

# CRUD
print("Read Database...")
results = read_CRUD()
for row in results:
    print(row)
print("Insert a record...")
create_CRUD("TestD15", "Sunny", "Hot", "High", "Weak", "Yes")
print("Read Database after create...")
results = read_CRUD()
for row in results:
    print(row)
print("Update a record...")
update_CRUD("TestD15", "Sunny", "Hot", "High", "Weak", "No", 15)
print("Read Database after update...")
results = read_CRUD()
for row in results:
    print(row)
print("Delete a record...")
delete_CRUD(15)
print("Read Database after delete...")
results = read_CRUD()
for row in results:
    print(row)
