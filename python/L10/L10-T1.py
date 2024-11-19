# L10-T1: Employee dictionary
#
# Submitted by: Md Hamidur Rahman Khan
#

data_types = {
    "Name": str,
    "Workplace": str,
    "Age": int,
    }

def get_input_by_type(type_: type, prompt: str):
    try:
        return type_(input(prompt))
    except:
        print("Invalid input")
        return get_input_by_type(type_, prompt)

def employee_dictionary(dict_list: list):
    employee = {}
    for data, type in data_types.items():
        value = get_input_by_type(type, f"Enter worker's {data.lower()}:\n")
        employee[data] = value
    dict_list.append(employee)

def print_work_info(dict_list: list):
    print("List of Employees:")
    for employee in dict_list:
        for data in data_types.keys():
            end = ", "
            if data == list(data_types.keys())[-1]:
                end = "\n"
            print(f"{data}: {employee[data]}", end=end)

def main():
    dict_list = []
    employee_count = int(input("How many employees do you want to add?:\n"))
    for _ in range(employee_count):
        employee_dictionary(dict_list)
    print_work_info(dict_list)
    
main()