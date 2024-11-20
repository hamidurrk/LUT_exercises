import json

menu_options = {
    "1": "Print students by age",
    "2": "Print students based on the course they are taking",
    "3": "Print students whose first names ends with the letter \"a\"",
    "0": "Stop the program"
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

def print_by_column(student_list, *args):
    for student in student_list:
        count = 1
        for arg in args:
            if arg == "id":
                info_specifier = "Student ID"
            elif arg == "courses":
                info_specifier = "Course"
            else:
                info_specifier = arg.capitalize()
            if count == len(args):
                print(f"{info_specifier}: {student[arg]}", end="\n")
            else:
                print(f"{info_specifier}: {student[arg]}", end=", ")
            count += 1

def filter_students_by_age(student_list, age):
    return [student for student in student_list if student["age"] == age]

def filter_students_by_course(student_list, course):
    return [student for student in student_list if course in student["courses"]]

def filter_students_by_first_name_last_char(student_list, char="a"):
    return [student for student in student_list if student["name"].split()[0][-1] == char]

def print_prompt_and_return_input(prompt: str, data):
    print(prompt)
    for index, item in enumerate(data):
        print(f"{index+1}) {item}")
    selection = get_input_by_type(int, "Enter your selection:\n")
    if 1 <= selection <= len(data):
        return data[selection-1]
    else:
        print("Invalid selection.")
        return None

def print_students_by_age(student_list):
    ages = [19,20,21,22]
    prompted_age = print_prompt_and_return_input("Select the age:", ages)
    if prompted_age != None:
        print_by_column(filter_students_by_age(student_list, prompted_age), "id", "name", "age")

def print_students_by_course(student_list):
    courses = ["Computer Science", "History", "Math", "Art"]
    prompted_course = print_prompt_and_return_input("Select the course:", courses)
    if prompted_course != None:
        print_by_column(filter_students_by_course(student_list, prompted_course), "id", "name", "courses")

def print_students_name(student_list):
    print("Students whose name end with 'a':")
    print_by_column(filter_students_by_first_name_last_char(student_list), "id", "name")

def menu():
    print("What do you want to do?")
    for key, value in menu_options.items():
        print(f"{key}) {value}")
    try:
        option_choice = int(input("Enter your choice:\n"))
        option = menu_options[str(option_choice)]
    except:
        option = "Invalid"
    return option

def main():
    try:
        file = open("./python/L10/files/students_short.json", mode = 'r')
        student_list = json.load(file)
    except:
        print("The file 'students.json' could not be found.")
        return

    while True:
        option = menu()
        match option:
            case "Print students by age":
                print_students_by_age(student_list)
            case "Print students based on the course they are taking":
                print_students_by_course(student_list)
            case "Print students whose first names ends with the letter \"a\"":
                print_students_name(student_list)
            case "Invalid":
                print("Invalid choice. Please try again.")
            case "Stop the program":
                print("See you again!")
                break
        print("")
main()

