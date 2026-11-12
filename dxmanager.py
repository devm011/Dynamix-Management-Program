
print(" =================================================")
print(" =                                               =")
print(" =        DYNAMIX MANAGEMENT PROGRAM             =")
print(" =                                               =")
print("==================================================")

while True:

    print("\n--------------- MAIN MENU ----------------")
    print("1. About Dynamix")
    print("2. Event Management")
    print("3. Participants")
    print("4. DX Team")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        while True:
            print("\n----------- ABOUT DYNAMICS -----------")
            print("0. Exit")

            option = input("\nEnter your choice: ")

            if option == "0":
                break

    elif choice == "2":
        while True:
            print("\n----------- EVENT MANAGEMENT -----------")
            print("0. Exit")

            option = input("\nEnter your choice: ")

            if option == "0":
                break

    elif choice == "3":
        while True:
            print("\n----------- PARTICIPANTS -----------")
            print("0. Exit")

            option = input("\nEnter your choice: ")

            if option == "0":
                break

    elif choice == "4":
        while True:
            print("\n----------- DX TEAM -----------")
            print("0. Exit")

            option = input("\nEnter your choice: ")

            if option == "0":
                break

    elif choice == "5":
        print("\nThank you for using Dynamix Management Program!")
        break

    else:
        print("\nInvalid choice! Please try again.")
