# L08-T5: try-except
#
# Submitted by: Md Hamidur Rahman Khan
#

from datetime import datetime

date_input = input("Enter a date in YYYY-MM-DD format:\n")

try:
    date_obj = datetime.strptime(date_input, "%Y-%m-%d")
    print(f"{date_input} is a valid date.")
except ValueError:
    print(f"{date_input} is not a valid date.")