from customer_account import CustomerAccount

cust1 = CustomerAccount()


def welcome_screen():
    print("**** Welcome to Access Bank  System ****")
    user_input = int(input("1. Show Balance \n 2.Withdraw \n 3. deposit \n 4. Cancel\n\n""provide require: "))

    user_options(user_input)


def user_options(user_input):
    if user_input == 1:
        show_user_balance()
    elif user_input == 2:
        user_withdraw()
    elif user_input == 3:
        user_deposit()
    elif user_input == 4:
        user_cancel()
    else:
        print("Invalid Require, Try Again")
    welcome_screen()


def show_user_balance():
    print(f"Your Account Balance is :GH¢ {cust1.check_balance()}")


def user_deposit():
    amount = float(input("Enter Amount: "))
    if amount > 0:
        cust1.deposit(amount)
        print(f" An Amount of GH¢ {amount}  has been deposited into Account successful")
    else:
        print("Invalid Amount Provide, Successful")


def user_withdraw():
    amount = float(input("Enter the Amount to Withdraw: "))
    if amount > 0:
        if not amount > cust1.check_balance():
            cust1.withdraw(amount)
            print(f" An Amount of GH¢ {amount} has been withdraw Successful From Your Account.")
    else:
        print("Not Eligible to Withdraw")


def user_cancel():
    print("Thank You for Banking with us at Access Bank, Hope to see you ")
    exit()


welcome_screen()
