shopping_list = []

def add_product():
    product = input("Enter the product to be added:\n")
    shopping_list.append(product)

def remove_product():
    print(f"You have {len(shopping_list)} products in your shopping list.")
    index = int(input("Enter the location of the product to be removed:\n"))
    shopping_list.pop(index-1)

def main():
    while True:
        print("Your shopping list contains the following products:")
        print(shopping_list)

        choice = int(input("Your choice:\n"))

        if choice == 1:
            add_product()
        elif choice == 2:
            remove_product()
        elif choice == 0:
            break
        else:
            print("Unknown selection.")
        print()
    print("You're going to buy the following products:")
    print(shopping_list)

main()
