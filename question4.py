# Age Calculator  
from datetime import datetime 
#current year
current_year = datetime.now().year

#  input
birth_year = int(input("Enter your birth year: "))

age = current_year - birth_year
months = age * 12
days = age * 365
hours = days * 24
minutes = hours * 60
years_to_100 = 100 - age

print("\nResults:")
print("Current Age:", age)
print("Age in Months:", months)
print("Age in Days (approx):", days)
print("Age in Hours:", hours)
print("Age in Minutes:", minutes)
print("Years until 100:", years_to_100)
