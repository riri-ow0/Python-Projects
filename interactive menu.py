total = 0

while True:
    try:
        choice = int(input("\n=====Interactive Menu=====\n[1] Burger (₱120)\n[2] Pizza (₱250)\n[3] Pasta (₱180)\n[4] Fried Chicken (₱150)\n[5] Softdrinks (₱50)\nPlease Enter your Choice: "))
        if choice < 1 or choice > 5:
            print("Please input a valid number!")
            continue
    except ValueError:
        print("Please input a valid number!")
        continue
    if choice == 1:
        try:
            c1 = int(input("How many Burger/s?: "))
            if c1 < 0:
                print("Please enter a valid amount!")
                continue
            else:
                cost = 120 * c1
                total += cost
                print("You've Ordered Burger/s that costs ₱", cost, "!")
        except ValueError:
            print("Please enter a valid amount!")
            continue
    elif choice == 2:
        try:
            c2 = int(input("How many Pizza/s?: "))
            if c2 < 0:
                print('Please enter a valid amount!')
                continue
            else:
                cost = 250 * c2
                total += cost
                print("You've Ordered Pizza/s that costs ₱", cost,"!")
        except ValueError:
            print('Please enter a valid number!')
            continue
    elif choice == 3:
        try:
            c3 = int(input("How many Pasta/s?: "))
            if c3 < 0:
                print('Please enter a valid amount!')
                continue
            else:
                cost = 180 * c3
                total += cost
                print("You've Ordered Pasta/s that costs ₱", cost, "!")
        except ValueError:
            print('Please enter a valid number!')
            continue
    elif choice == 4:
        try:
            c4 = int(input("How many Fried Chicken/s?: "))
            if c4 < 0:
                print('Please enter a valid amount!')
                continue
            else:
                cost = 150 * c4
                total += cost
                print("You've Ordered Fried Chicken/s that costs ₱", cost, "!")
        except ValueError:
            print('Please enter a valid number!')
            continue
    elif choice == 5: 
        try:
            c5 = int(input("How many Softdrink/s?: "))
            if c5 < 0:
                print('Please enter a valid amount!')
                continue
            else:
                cost = 50 * c5
                total += cost
                print("You've Ordered Softdrink/s that costs ₱", cost, "!")
        except ValueError:
            print('Please enter a valid number!')
            continue
    option = input("Would you like to order again?[y/n]: ")
    if option == "y" or option == "Y":
        continue   
    else: 
        print("Thank you for ordering!")
        print("Your total is ₱", total)
        break
