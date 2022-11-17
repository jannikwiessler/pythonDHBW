from workshop_data import data
from functions import average_mileage

print(f"average mileage: {average_mileage(data)}")
print(f"average mileage of A-Class: {average_mileage(data,'A-Class')}")
print(f"average mileage of S-Class: {average_mileage(data,'S-Class')}")