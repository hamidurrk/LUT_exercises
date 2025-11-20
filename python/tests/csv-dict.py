import csv

filename = "python/tests/test.csv"

try:
    file = open(filename, "r")
    reader = csv.DictReader(file)
    # print(reader.fieldnames)
    sum_result = 0.0

    for row in reader:
        print(row)
        columns = list(row.keys())
        value = float(row[columns[1]])
        sum_result += value

    file.close()

    sum_result = round(sum_result, 2)
    print("Sum of the second column:", sum_result)

except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Invalid numeric data in CSV.")