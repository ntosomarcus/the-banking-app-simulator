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
    
    print("""
    1. Deposit
    2. Withdraw
    3. Transfer money
    4. Paybill
        """)
    choice = int(input("Choose the transaction you want today: "))
    if choice == 1:
        amount = float(input(f"{name} how much do you want to deposit? \n"))
        deposit = t.deposit(amount)
    elif choice == 2:
        amount = float(input("how much do you want to withdraw? \n"))
        withdraw = t.withdraw(amount)
        print(withdraw)
        return choice
            

        
            


if __name__ == "__main__":
    main()