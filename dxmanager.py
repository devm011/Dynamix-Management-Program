


events = ["Dynamix 2K26","Fragfest'26","Fragfest'27","Dynamix 2K27"]
import time
time.sleep(0.9)
print("Loading...")
time.sleep(0.8)
print("Almost done...")
time.sleep(0.5)

while True:
    print('''
  ____                              _          __  __                                                   _   
 |  _ \ _   _ _ __   __ _ _ __ ___ (_)_  __   |  \/  | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_ 
 | | | | | | | '_ \ / _` | '_ ` _ \| \ \/ /   | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|
 | |_| | |_| | | | | (_| | | | | | | |>  <    | |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_ 
 |____/ \__, |_| |_|\__,_|_| |_| |_|_/_/\_\   |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|
        |___/                                                           |___/                               
                     MADE BY Manavdeep Singh
        
        
        ''')



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
            print('''

============================================================
                       ABOUT DYNAMIX
============================================================

WHO WE ARE
-----------
Dynamix is our school's technology club. It introduces students
to technology, computing and digital innovation, and gives them
a place to explore beyond the classroom.

WHAT WE DO
----------
Students get to explore coding, game development, animation,
photography, videography, graphic design and other creative
areas of technology.

LEARNING TOGETHER
-----------------
Dynamix encourages students to try new things, develop ideas,
solve problems and show what they can create. It also brings
students together through technology-based events and
competitions.

OUR EVENTS
----------
Dynamix 2026 marked the club's 25th anniversary, featuring
25 different activities.

FragFest is an inter-house technology competition organised
by the Dynamix team in collaboration with a school house.
It gives students a chance to take part in technology-related
challenges.

MORE THAN TECHNOLOGY
--------------------
Dynamix is not just about computers and competitions. It helps
students build logical thinking, creativity, teamwork and
confidence.

============================================================
          CURIOSITY  |  CREATIVITY  |  INNOVATION
============================================================

''')
            print("0. Exit")

            option = input("\nEnter your choice: ")

            if option == "0":
                break

    elif choice == "2":
        while True:
            print("\n----------- EVENT MANAGEMENT -----------")
            print("1. Show All Events")
            print("2. Add")
            print("3. delete")
            print("0. Exit")

            option = input("\nEnter your choice: ")

            if option == "1":
                while True:
                    print("\n---------EVENTS-----------")
                    for x in range(len(events)):
                        print(f"{x+1}. {events[x]}")
                    print("0. exit")

                    option = input("\nEnter you choice: ")

                    if option != "0":
                        while True:
                            print("Sorry! we are working on this option! :)")
                            print("0. exit")
                            option = input("Enter you choice: ")

                            if option == "0":
                                break
                            else:
                                pass
                    else:
                        break

            elif option == "2":
                while True:
                    print("What event would you like to add?")
                    print("0. exit")
                    new_event = input("\nEnter a Event Name - ")
                    if new_event != "0":
                        events.append(new_event)
                        print(f"New event has been added! {new_event}")
                        time.sleep(1.2)
                        print("Returning to main menu...")
                        time.sleep(1.2)
                        break
                    else:
                        break

            elif option == "3":
                while True:
                    print("What events would you like to remove")
                    
                    print("0. exit")
                    for i in range(len(events)):
                        print(f"{i+1}. {events[i]}")

                    remove_event = int(input("\nEnter Your Choice: "))

                    if remove_event != 0:
                      removed_event = events.pop(remove_event - 1)
                      print(f"{removed_event} has been removed.")
                      time.sleep(1.2)
                      print("returning back to menu screen...")
                      time.sleep(1.2)
                      break
                    else:
                        break

            elif option == "0":
                break

                
                        
    elif choice == "3":
        while True:
            print("\n----------- PARTICIPANTS -----------")
            print("Sorry! we are working on this option! :)")
            print("0. Exit")

            option = input("\nEnter your choice: ")

            if option == "0":
                break
            else:
                pass

    elif choice == "4":
        while True:
            print("\n----------- DX TEAM -----------")
            print("Sorry! we are working on this option! :)")
            print("0. Exit")

            option = input("\nEnter your choice: ")

            if option == "0":
                break
            else:
                pass

    elif choice == "5":
        print("\nThank you for using Dynamix Management Program!")
        break

    else:
        print("\nInvalid choice! Please try again.")
