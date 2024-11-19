# L10-T3: Titanic Passenger Data Processing
#
# Submitted by: Md Hamidur Rahman Khan
#

import csv

csv_file = open('titanic.csv', mode='r')
data = csv.DictReader(csv_file)
reader = list(data)

def calculate_discrete_average(col):
    entries = []
    for row in reader:
        if row[col]:
            entries.append(float(row[col]))
    return round(sum(entries) / len(entries))

def nominal_count(col, value):
    count = 0
    for row in reader:
        if row[col] == value:
            count += 1
    return count

def get_discrete_max(col):
    entries = []
    for row in reader:
        if row[col]:
            entries.append(float(row[col]))
    return round(max(entries))

print(f"The number of male passengers: {nominal_count("Sex", "male")}")
print(f"The number of female passengers: {nominal_count("Sex", "female")}")
print(f"The average age of passengers: {calculate_discrete_average("Age")}")
print(f"The age of the oldest passenger: {get_discrete_max("Age")}")
