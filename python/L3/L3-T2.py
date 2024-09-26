option = input("Do you want to stop the execution of the program (Y/N):\n")

if (option == "Y"):
    print ("Bye!")
elif (option == "N"):
    username = input("Enter username:\n")
    password = input("Enter Password:\n")
    
    if (username == "pekka" and password == "somerandomthing"):
        print("User recognized!")
    else:
        print("You entered an invalid login name or password.")
else:
    print("Invalid input! Please try again.")