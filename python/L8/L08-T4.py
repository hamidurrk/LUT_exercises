# L08-T4: Python library: datetime
#
# Submitted by: Md Hamidur Rahman Khan
#

from datetime import datetime, timedelta

operations = {
    "1": "Identify the components of a time object",
    "2": "Calculate age in days",
    "3": "Print the days of the week",
    "4": "Print the months ",
    "0": "Stop"
}

def menu():
    print("What do you want to do:")
    for key, value in operations.items():
        print(f"{key}) {value}")
    try:
        option = operations[input("Your choice:\n")]
    except:
        option = "Invalid"
    return option

def identify_components():
    date_str = input("Enter the date and time in the format 'dd.mm.yyyy hh:mm':\n")
    try:
        dt_obj = datetime.strptime(date_str, "%d.%m.%Y %H:%M")
        print(f"You gave year {dt_obj.year}")
        print(f"You gave month {dt_obj.month}")
        print(f"You gave day {dt_obj.day}")
        print(f"You gave hour {dt_obj.hour}")
        print(f"You gave minute {dt_obj.minute}")
    except ValueError:
        print("Invalid date format. Please use 'dd.mm.yyyy hh:mm'.")

def calculate_age_in_days():
    birth_date_str = input("Enter your birthday as dd.mm.yyyy:\n")
    try:
        birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y")
        start_of_2024 = datetime(2024, 1, 1)
        age_in_days = (start_of_2024 - birth_date).days
        print(f"On January 1, 2024, you were {age_in_days} days old.")
    except ValueError:
        print("Invalid date format. Please use 'dd.mm.yyyy'.")

def print_days_of_week():
    monday_date = datetime(2024, 1, 1)  
    for i in range(7):
        day = monday_date + timedelta(days=i)
        print(day.strftime("%A"))

def print_months():
    for i in range(1, 13):
        month_date = datetime(2024, i, 1)
        print(month_date.strftime("%b"))
        
def main():
    print("This program uses the datetime library to deal with time.")
    while True:
        option = menu()
        
        match option:
            case "Identify the components of a time object":
                identify_components()
            case "Calculate age in days":
                calculate_age_in_days()
            case " Print the days of the week":
                print_days_of_week()
            case "Print the months":
                print_months()
            case "Stop":
                print("See you again!")
                break
            case "Invalid":
                print("Unknown choice, please try again.")
        print("")
main()