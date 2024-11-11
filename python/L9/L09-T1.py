# L09-T1: “None” in Python
#
# Submitted by: Md Hamidur Rahman Khan
#

def input_integer():
    try:
        int_input = int(input("Enter an integer:\n"))
        return int_input
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None

def prompt_and_add(iteration, count=0, integers=[]):
    if count < iteration:
        int_input = input_integer()
        if int_input is not None:
            integers.append(int_input)
            count += 1
        return prompt_and_add(iteration, count, integers)
    return integers

def main():
    iteration = input_integer()
    if iteration is None:
        return main()
    print(f"Now give {iteration} integers!")
    integers = prompt_and_add(iteration)
    print("The sum of the entered integers is:", sum(integers))
    
main()