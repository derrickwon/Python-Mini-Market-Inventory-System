from product import Product
# empty dictionary declare
inventory = {"apple":Product("Apple","Fruits" , 5,2.99)}

# add_item function body
def add_item():
    item_name = input("Enter item name: ").lower() #case-sensitive, to avoid same name
    if item_name not in inventory:
        item_cat = input("Enter item category: ").lower()
        item_quantity = int(input("Enter item quantity: "))
        item_unit_price = float(input("Enter item unit price: "))
        # to validate item quantity is >0 and price is > 0
        if item_quantity <=0 or item_unit_price <=0:
            print("Invalid input. Please input positive numbers.")
        else:
            # pass argument to creates object an object in dictionary
            inventory[item_name] = Product(item_name, item_cat, item_quantity, item_unit_price)
            print("Item added successfully!")
    else:
        print("Item already exists!")

# view_inventory function body
def view_inventory():
    if inventory == {}:
        print("Inventory is empty!")
        return
    print("Sorting Options:")
    print("1. By Name(A-Z)")
    print("2. By Category(A-Z)")
    print("3. By Quantity(ascending)")
    print("4. By Quantity(descending)")
    print("5. By Total Value (ascending)")
    print("6. By Total Value (descending)")

    option = input("Enter option: ")

    #Creating a list with value of inventory
    items = list(inventory.values())
    match option:
        case "1":
            items.sort(key=Product.get_name)
        case "2":
            items.sort(key=Product.get_category)
        case "3":
            items.sort(key=Product.get_quantity)
        case "4":
            items.sort(key=Product.get_quantity, reverse=True)
        case "5":
            items.sort(key=Product.get_total_value)
        case "6":
            items.sort(key=Product.get_total_value, reverse=True)
        case _:
            print("Out of range! Try again.")

    print("\nName\tCategory\tQuantity\tUnit Price\tTotal Value")
    print("=========================================================")
    for i in items:
        i.display()

def update_item():
    if inventory == {}:
        print("Nothing to edit!")
        return
    print()
    print("\nName\tCategory\tQuantity\tUnit Price\tTotal Value")
    print("=========================================================")
    items = list(inventory.values())
    for i in items:
        i.display()
    item_name = input("Enter item name that you want to edit: ").lower()
    if item_name not in inventory:
        print("Item does not exist!")
        return
    product = inventory[item_name]
    print("What would you like to edit?")
    print("1. Category")
    print("2. Quantity")
    print("3. Unit Price")
    option = input("Enter option: ")
    match option:
        case "1":
            new_category = input("Enter new category: ").lower()
            product.category = new_category
            print("Category updated successfully!")
        case "2":
            new_quantity = int(input("Enter new quantity: "))
            if new_quantity < 0:
                print("Invalid input..")
            else:
                product.quantity = new_quantity
                print("Item quantity updated successfully!")
        case "3":
            new_unit_price = float(input("Enter new unit price: "))
            if new_unit_price <= 0:
                print("Invalid price..")
            else:
                product.unit_price = new_unit_price
                print("Item unit price updated successfully!")
        case _:
            print("Out of range! Try again.")


#search_item function body
def search_item():
    item_name = input("Enter item name: ").lower()
    if item_name in inventory:
        print("\nName\tCategory\tQuantity\tUnit Price\tTotal Value")
        print("=========================================================")
        Product.display(inventory[item_name])
    else:
        print(f"No item named '{item_name}' found in the inventory!")


#Remove item function body
def remove_item():
    item = input("Enter Item name to remove: ").lower()
    if item in inventory:
        confirm = input(f"Are you sure you want to remove {item} from inventory?(y/n): ").lower()
        if confirm == 'y':
            # delete the input item from inventory if found
            del inventory[item] 
            print(f"Item '{item}' removed successfully.")
        else:
            print("Process terminated.")
    else:
        print("Item not found in inventory")
    print("Redirecting to Main Menu...")

# Generate Report function body
def generate_report():
    if inventory == {}:
        print("Inventory is empty.")
        return

    #initial value to store calculated index
    total_value = 0
    highest_value_item = 0
    lowest_quantity_item = 0

    # loop through the inventory
    for i in inventory.values():
        total_value += i.calculate_value()

        # check for highest-value item
        if highest_value_item ==0 or i.calculate_value() > highest_value_item.calculate_value():
            highest_value_item = i

        # check for lowest-quantity item
        if lowest_quantity_item ==0 or i.get_quantity() < lowest_quantity_item.get_quantity():
            lowest_quantity_item = i
    #print function to print result
    print("\n============ Inventory Report ============")
    print(f"Total Inventory Value: RM{total_value:.2f}")
    print(f"Highest-Value Item: {highest_value_item.get_name()} [Value = RM{highest_value_item.calculate_value():.2f}]")
    print(f"Lowest-Quantity Item: {lowest_quantity_item.get_name()} [Quantity = {lowest_quantity_item.get_quantity()} units]")
    print("==========================================")
