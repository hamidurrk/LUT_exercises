# L07-T5: Menu-based program - calculator. Continues from L05-T5
#
# Submitted by: Md Hamidur Rahman Khan
#

# Declaring variables without assigning values
num1: int
num2: int

# Dictionary of operations
operations = {
    "1": "Enter the values",
    "2": "Sum",
    "3": "Subtract",
    "4": "Multiply",
    "5": "Divide",
    "0": "Stop"
}

def menu():
    print("This calculator can perform the following functions:")
    for key, value in operations.items():
        print(f"{key}) {value}")
    option = operations[input("Select the function (0-5):\n")]
    return option

def read_value(stream) -> int:
    data = stream.readline().strip()
    if data == '':
        print("End of values, end the program.")
        return 0
    return int(data)

def write_data(stream, data: str):
    stream.write(f"{data}\n")
    print("Result saved in file.")

def sum(value1: int, value2: int) -> str:
    return (f"sum {value1} + {value2} = {value1+value2}")
 
def subtract(value1: int, value2: int) -> str:
    return (f"subtract {value1} - {value2} = {value1-value2}")

def multiplication(value1: int, value2: int) -> str:
    return f"multiply {value1} * {value2} = {value1*value2}"

def division(value1: int, value2: int) -> str:
    if (value2 == 0):
        return "Cannot divide by zero."
    else:
        return f"division {value1} / {value2} = {round(value1/value2, 2)}"

def main():
    source_name = input("Enter the name of the file to read:\n")
    source = open(source_name, "r")
    results_file = open("Exercise5_output.txt", "w")
    while True:
        option = menu()
        match option:
            case "Enter the values":
                num1 = read_value(source)
                num2 = read_value(source)
                print(f"Values {num1} and {num2} were read")
            case "Sum":
                write_data(stream=results_file, data=sum(num1, num2))
            case "Subtract":
                write_data(stream=results_file, data=subtract(num1, num2))
            case "Multiply":
                write_data(stream=results_file, data=multiplication(num1, num2))
            case "Divide":
                write_data(stream=results_file, data=division(num1, num2))
            case "Stop":
                print("Stopping")
                break
    source.close()
    results_file.close()
        
if __name__ == "__main__":
    main()