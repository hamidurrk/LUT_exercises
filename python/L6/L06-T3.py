# L06-T3: Menu-based program for shopping list processing
#
# Submitted by: Md Hamidur Rahman Khan
#

shopping_list = []
functions = {
    "1": "Add",
    "2": "Remove",
    "0": "End"
}

def add(list : list):
    product = input("Enter the product to be added:\n")
    list.append(product)

def remove(list : list):
    if not len(shopping_list) < 1:
        try:
            print(f"You have {len(shopping_list)} items in your shopping list.")
            index = int(input("Enter the location of the product to be removed:\n"))
            list.pop(index - 1)
        except IndexError:
            print("Invalid index.")
    else:
        print("Your shopping list is already empty.")

def menu():
    print(f"Your shopping list contains the following products:\n{shopping_list}")
    print("You can choose from the functions below:")
    for key, value in functions.items():
        print(f"{key}) {value}")
    try:
        option = functions[input("Your choice:\n")]
    except KeyError:
        print("Unknown selection.")
        return None
    return option

def main():
    while True:
        option = menu()
        
        match option:
            case "Add":
                add(shopping_list)
            case "Remove":
                remove(shopping_list)
            case "End":
                print(f"You are going to buy the following products:\n{shopping_list}")
                break
        print("")
        
if __name__ == "__main__":
    main()