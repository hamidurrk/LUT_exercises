# L10-T2: Employee dictionary 2
#
# Submitted by: Md Hamidur Rahman Khan
#

employee_dict = [
    {'Name': 'John', 'Workplace': 'LUT', 'Age': 25},
    {'Name': 'Jack', 'Workplace': 'Finnair', 'Age': 18},
    {'Name': 'Robin', 'Workplace': 'JBL', 'Age': 32},
    {'Name': 'Annie', 'Workplace': 'LUT', 'Age': 24},
    {'Name': 'Niels', 'Workplace': 'Microsoft', 'Age': 45}
]

data_types = {
    "Name": str,
    "Workplace": str,
    "Age": int,
}

def get_input_by_type(type_: type, prompt: str):
    try:
        return type_(input(prompt))
    except:
        if type_ == int:
            print("Invalid input. Please enter a number.")
        elif type_ == str:
            print("Invalid input. Please enter a string.")
        else:
            print("Invalid input. Please enter a valid value.")

def print_work_info(dict_list: list):
    print("List of Employees:")
    for employee in dict_list:
        for data in data_types.keys():
            end = ", "
            if data == data_types.keys()[-1]:
                end = "\n"
            print(f"{data}: {employee[data]}", end=end)

def main():
    # print_work_info(employee_dict)
    print(list(employee_dict[0].keys())[-1])
    
main()