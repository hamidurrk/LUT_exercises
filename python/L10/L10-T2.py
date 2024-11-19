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

menu_options = {
    "1": "Remove an employee",
    "2": "Modify employee data",
    "3": "Print all employees",
    "0": "Exit"
}

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
        return None

def search_data(name=None, workplace=None, age=None, index=None, dict_list=employee_dict):
    try:
        if name != None:
            for employee in dict_list:
                if employee["Name"] == name:
                    return employee
        elif workplace != None:
            for employee in dict_list:
                if employee["Workplace"] == workplace:
                    return employee    
        elif age != None:
            for employee in dict_list:
                if employee["Age"] == age:
                    return employee
        elif index != None:
            index -= 1
            return dict_list[index]
        else:
            return None
    except IndexError:
        print("Invalid index. Please enter a valid index.")
        return None
    
def process_data(new_workplace=None, new_age=None, dict_list=employee_dict, dict=None):
    index = employee_dict.index(dict)
    if new_workplace != None:
        dict_list[index]["Workplace"] = new_workplace
        return None
    elif new_age != None:
        dict_list[index]["Age"] = new_age
        return None
    if new_workplace == None and new_age == None:
        employee_dict.remove(dict)
        return dict["Name"]
    if dict == None:
        return None

def print_work_info(dict_list: list, indexed=False):
    print("List of Employees:")
    for employee in dict_list:
        if indexed:
            print(f"{dict_list.index(employee) + 1}", end=") ")
        for data in data_types.keys():
            end = ", "
            if data == list(data_types.keys())[-1]:
                end = "\n"
            print(f"{data}: {employee[data]}", end=end)
            
def remove_employee(employee_list):
    print_work_info(employee_list, indexed=True)
    index = get_input_by_type(int, "Enter the number of the employee to remove:\n")
    if index != None:
        removed_name = process_data(dict_list=employee_list, dict=search_data(index=index, dict_list=employee_list))
        if removed_name != None:
            print(f"Removed employee: {removed_name}")

def modify_employee(employee_list):
    print_work_info(employee_list, indexed=True)
    index = get_input_by_type(int, "Enter the number of the employee to modify:\n")
    if index != None:    
        field = get_input_by_type(int, "Enter the field to modify:\n1) Workplace\n2) Age\n")
        if field == 1:
            new_workplace = get_input_by_type(str, "Enter new value for Workplace:\n")
            process_data(new_workplace=new_workplace, dict_list=employee_list, dict=search_data(index=index, dict_list=employee_list))
        elif field == 2:
            new_age = get_input_by_type(int, "Enter new value for Age:\n")
            process_data(new_age=new_age, dict_list=employee_list, dict=search_data(index=index, dict_list=employee_list))
        else:
            print("Invalid field. Please enter a valid field.")

def print_employee(employee_list):
    print_work_info(employee_list)
    
def menu():
    print("Menu:")
    for key, value in menu_options.items():
        print(f"{key}) {value}")
    try:
        while True:
            try:
                option_choice = int(input("Enter your choice:\n"))
                break
            except ValueError:
                print("Enter the selection as an integer.")
        option = menu_options[str(option_choice)]
    except:
        option = "Invalid"
    return option

def main():
    while True:
        option = menu()
        match option:
            case "Remove an employee":
                remove_employee(employee_dict)
            case "Modify employee data":
                modify_employee(employee_dict)
            case "Print all employees":
                print_employee(employee_dict)
            case "Invalid":
                print("Unknown selection, please try again.")
            case "Exit":
                print("See you again!")
                break
    
main()