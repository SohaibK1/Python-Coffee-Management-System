def coffee_management_system():
    print("Welcome to Coffee Management System")
    print("Menu:\n1. Black Coffee - $2.00\n2. Espresso - $2.50\n3. Latte - $3.00")
    choice = input("Select an option (1/2/3): ")

    prices = {'1': 2.00, '2': 2.50, '3': 3.00}

    if choice not in prices:
        print("Invalid Option")
        return

    print("Do you want to customize your order or go with standard?")
    custom_choice = input("Type 'customize' or 'standard': ").lower()

    if custom_choice == 'customize':
        water = input("Add Water? (yes/no): ").lower()
        coffee_level = input("Set Coffee Level (High/Medium/Low): ").capitalize()
        milk_level = input("Set Milk Level (High/Medium/Low): ").capitalize()
        sugar = input("Add Sugar? (yes/no): ").lower()
    else:
        print("Proceeding with standard preparation...")

    try:
        quantity = int(input("Enter Order Quantity: "))
    except ValueError:
        print("Invalid Quantity")
        return

    total = quantity * prices[choice]
    print(f"Total Bill: ${total:.2f}")

    print("Select Payment Method:\n1. Cash\n2. Card")
    payment_method = input("Choose (1/2): ")

    if payment_method == '1':
        try:
            paid = float(input("Enter Amount Paid: $"))
        except ValueError:
            print("Invalid Payment Amount")
            return
        remaining = total - paid
        if remaining > 0:
            print(f"Remaining Amount: ${remaining:.2f}")
        else:
            print(f"Change to return: ${-remaining:.2f}")
    elif payment_method == '2':
        print("Processing card payment...")
    else:
        print("Invalid Payment Method")
        return

    print("Print or Go Green?")
    print_choice = input("Type 'print' or 'go green': ").lower()
    if print_choice == 'print':
        print("Printing Bill...")
    else:
        print("Go Green! No paper bill.")
    print("Thank you for your order!")
coffee_management_system()
