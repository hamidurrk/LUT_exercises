option = input("Do you want to stop the execution of the program (Y/N):\n")
user = "Pekka"
password = "somerandomthing"

if option == "N":
    user_input = input("Enter username:\n")
    password_input = input("Enter password:\n")

    if user_input == user and password_input == password:
        print("User recognized!")
    else:
        print("You entered an invalid login name or password.")
elif option == "Y":
    print("Bye!")
else:
    print("Invalid input! Please try again.")
    
