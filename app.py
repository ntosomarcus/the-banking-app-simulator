from UserInfo import User_information
from transactions import Transactions
def main():
    t = Transactions()
    print(f"\nWelcome to the Banking App\n")
    print("******************************\n")

# allowing the user to enter details/information
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    account_number = input("Enter account number here: ")
    PIN = input("Enter PIN here: ")
    u = User_information(name,age,PIN,account_number)

    while True:  
        print("""
        1. Deposit
        2. Withdraw
        3. Transfer money
        4. Paybill
        5. exit 
            """)
        choice = int(input("Choose the transaction you want today: "))
        if choice == 1:
            amount = float(input(f"{name} how much do you want to deposit? \n"))
            deposit = t.deposit(amount)
            print(deposit)
        elif choice == 2:
            amount = float(input("How much do you want to withdraw? \n"))
            withdraw = t.withdraw(amount)
            print(withdraw)
        elif choice == 3:
            amount = float(input("How much do you want to Transfer?\n"))
            receipient = str(input("Enter receiver's name: "))
            t.transfer_money(name,amount,receipient)
        elif choice == 4:
            bill = str(input("Enter the type of Bill"))
            amount = float(input("How much do you want to pay? \n"))
            PayBill = t.paybills(amount,bill)
            print(PayBill)
        elif choice == 5:
            print("Thank you for banking with us.")
            break
        else:
            print("Invalid Input!")
            

        
            


if __name__ == "__main__":
    main()