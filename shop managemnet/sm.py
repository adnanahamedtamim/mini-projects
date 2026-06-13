print("\n//***********Mini Inventory System***********//")

inventory = {}

while True:
    print("\n\n1. Add Product")
    print("2. Update Stock")
    print("3. Low Stock Warning")
    print("4. View All Inventory")
    print("5. Quit")

    index = int(input("\nindex :: "))

    if index == 1:
        name = input("Enter product name: ")
        
        if name in inventory:
            print("\nProduct already exists!")
            continue
            
        qty = int(input("Enter initial quantity: "))
        thresh = int(input("Enter low stock threshold: "))
        
        inventory[name] = {
            "quantity": qty,
            "threshold": thresh
        }
        print("\nProduct added successfully")

    elif index == 2:
        name = input("Enter product name: ")
        
        if name not in inventory:
            print("\nProduct not found")
            continue
            
        print("1. Add Stock")
        print("2. Remove Stock")
        action = int(input("Enter action: "))
        amount = int(input("Enter amount: "))
        
        if action == 1:
            inventory[name]["quantity"] += amount
            print("\nStock added successfully")
        elif action == 2:
            if inventory[name]["quantity"] < amount:
                print("\nNot enough stock to remove!")
            else:
                inventory[name]["quantity"] -= amount
                print("\nStock removed successfully")
        else:
            print("\nInvalid action")

    elif index == 3:
        print("\n--- Low Stock Alerts ---")
        found_low_stock = False
        
        for item in inventory:
            if inventory[item]["quantity"] <= inventory[item]["threshold"]:
                print(item + " is running low! Current stock: " + str(inventory[item]["quantity"]))
                found_low_stock = True
                
        if found_low_stock == False:
            print("All products have sufficient stock.")

    elif index == 4:
        print("\n--- Current Inventory ---")
        for item in inventory:
            print("Product: " + item + " | Quantity: " + str(inventory[item]["quantity"]) + " | Threshold: " + str(inventory[item]["threshold"]))

    elif index == 5:
        print("\nExiting system. Goodbye!")
        break

    else:
        print("\nInvalid Index")
