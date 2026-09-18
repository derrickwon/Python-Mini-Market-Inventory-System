import time
import os
from inventory import add_item, view_inventory, search_item, update_item , remove_item , generate_report


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    Second_attempt = False
    while True:
        if Second_attempt == True:
            print()
            input("Press Enter to continue...")
        time.sleep(1)
        clear_screen()
        print("Inventory Management System")
        print("1. Add Item")
        print("2. View Items")
        print("3. Search Item")
        print("4. Update Item")
        print("5. Remove Item")
        print("6. Generate Reports")
        print("7. Exit")
        Second_attempt = True
        try: # handle non integer input
            choice = int(input("Enter your choice: "))
            time.sleep(1)
            clear_screen()
            match choice:
                case 1:
                    add_item()
                case 2:
                    view_inventory()
                case 3:
                    search_item()
                case 4:
                    update_item()
                case 5:
                    remove_item()
                case 6:
                    generate_report()
                case 7:
                    print("Thank you for using the system.\nExiting...")
                    time.sleep(2)
                    break
                case _:
                    print("Invalid choice. Please enter between 1 - 7.")
        except Exception as e:
            print(f"Invalid choice. Please enter between 1 - 7. Error code: {e}")

menu()