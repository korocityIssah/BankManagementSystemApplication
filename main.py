# Bank Application
from datetime import date

accountNo = 0
cusName = ""
Dob = ""
address = ""
nextK = ""
visit = ""
BCode = ""
Mobile = 0
Bal = 0
accountType = ""


def createAccounts():
    global accountNo
    global cusName
    global Dob
    global address
    global nextK
    global visit
    global BCode
    global Mobile
    global Bal
    global accountType
    cusName = input("Enter Customer Name: ")
    Dob = int(input("Enter Date of Birth..: "))
    address = input("Enter Customer Address: ")
    nextK = input("Enter Next of Kin: ")
    visit = input("Enter the Visitation: ")
    accountType = input("Enter the Account Type [Saving or Current]: ")
    accountNo = int(input("Enter the Account Number: "))
    BCode = input("Enter the Branch Code: ")
    Mobile = input("Enter Mobile Number: ")
    Bal = str(float(input("Enter the Current Balance: ")))


def showAccountDetails():
    print("CustomerName: " + cusName)
    print("Date of Birth: " + Dob)
    print("Address: " + address)
    print("Next of Kin: " + nextK)
    print("Visitation: " + visit)
    print("AccountType: " + accountType)
    print("AccountNo: " + accountNo)
    print("BranchCode: " + BCode)
    print("Mobile: " + Mobile)


def Deposit(amount):
    global Bal
    Bal = str(float(Bal) + float(amount))
    print(" An amount of GH¢" + str(float(amount)) + " has been Credited into your Account. ")
    checkbalance(amount)


def Withdraw(amount):
    global Bal
    Bal = str(float(Bal) - float(amount))
    print(" An amount of GH¢" + str(float(amount)) + " has been Debited from your Account. ")
    checkbalance(amount)


def checkbalance(amount):
    print(cusName + " Your Current Balance is: " + str(float(Bal)))


ch1 = "yes"
while ch1 == "yes":
    print("1. Create Account \n 2.Withdraw \n 3. deposit \n 4. Check Balance")
    ch = int(input("Select any option: "))
    if ch == 1:
        createAccounts()
    elif ch == 2:
        amount = float(input("Enter the Amount to Withdraw: "))
        Withdraw(amount)
    elif ch == 3:
        amount = str(float(input("Enter the Amount to Deposit: ")))
        Deposit(amount)
    elif ch == 4:
        checkbalance(Bal)
        print("Do you want to continue..  press [Yes or No]: ")
        ch1 = input()
        ch1 = str.lower(ch1)
    else:
        print("Please Select any of the 4 Option Available Above")
