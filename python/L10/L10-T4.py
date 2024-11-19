import json

def menu():
    print("What do you want to do?")
    print("1) Print students by age")
    print("2) Print students based on the course they are taking")
    print("3) Print students whose first names ends with the letter \"a\"")
    print("0) Stop the program")

def print_students_by_age(student_list):
    ages = [19,20,21,22]

    index = 1
    print("Select the ages of the students:")
    for age in ages:
        print(f"{index}) {age}")
        index += 1
    try:
        selection = int(input("Enter your selection:\n"))
        if 1 <= selection <= len(ages):
            selected_age = ages[selection-1]
            for student in student_list:
                if student["age"] == selected_age:
                    print(f"Student ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
        else:
            print("Invalid selection.")
    except:
        print("Invalid input.")

def print_students_by_course(student_list):
    courses = ["Computer Science", "History", "Math", "Art"]

    index = 1
    print("Select the course:")
    for course in courses:
        print(f"{index}) {course}")
        index += 1
    try:
        selection = int(input("Enter your selection:\n"))
        if 1 <= selection <= len(courses):
            selected_course = courses[selection-1]
            for student in student_list:
                if selected_course in student["courses"]:
                        print(f"Student ID: {student['id']}, Name: {student['name']}, Course: {student['courses']}")
        else:
            print("Invalid selection.")
    except:
        print("Invalid input.") 

def print_students_name(student_list):
    print("Students whose name end with 'a':")
    for student in student_list:
        first_name = student["name"].split()[0]
        if first_name[-1] == 'a':
            print(f"Student ID: {student['id']}, Name: {student['name']}")

def main():
    try:
        file = open("students.json", mode = 'r')
        student_list = json.load(file)
        #print(student_list)
    except:
        print("The file 'students.json' could not be found.")
        return

    while True:
        menu()
        try:
            choice = int(input("Enter your choice:\n")) 
        except:
            pass
        if choice == 1:
            print_students_by_age(student_list)
        elif choice == 2:
            print_students_by_course(student_list)
        elif choice == 3:
            print_students_name(student_list)
        elif choice == 0:
            print("See you again!")
            break
        else:
            print("Invalid choice. Please try again.")
        print("")
main()

