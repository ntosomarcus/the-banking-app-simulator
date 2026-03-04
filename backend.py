class Transactions:
    def __init__(self):
        self.balance = 0
        account_details = {}
        
    def deposit(self,amount: float):
        if amount > 0:
            self.balance += amount 
            return(f"You have ${amount} deposited.\nCurrent balance is ${self.balance}")
        else:
            return( f"You can't deposit ${amount}, Invalid amount" )

    def withdraw(self,amount: float):
        if amount <= 0:
            return f"You can't withdraw ${amount}, invalid amount"
        elif amount > self.balance:
            return f"You can't withdraw ${amount}, your balance is ${self.balance}"
        else:
            self.balance -= amount
            return f"${amount} withdrawn\nCurrent balance is ${self.balance}"
        
    def transfer_money(self,sender: str,amount: float,receiver: str):
        if amount <= self.balance:
            self.balance = self.balance - amount
            return( f"Transfer to {receiver} successful! current balance is ${self.balance}")
        elif amount > self.balance:
            return( f"You can't transfer ${amount}, your balance is ${self.balance}")

    def view_balance(self):
        print( f"Balance: ${self.balance}")
    
    def paybills(self,amount: float,bill: str):
        if amount < self.balance :
            self.balance -= amount
            print( f"${amount} {bill} paid successfully!" )
            return self.view_balance()
        elif amount < 0 or amount > self.balance:
            print("Invalid amount/Insufficient balance")


class User_information(Transactions):
    def __init__(self,name: str,age: int,PIN: int, account_num):
        self.name = name 
        self.age = age
        self.PIN = PIN
        self.account_details = {"name":  
                                {"transaction": []}
                                }
    def get_name(self):
        if isinstance(self.name,str):
            self.account_details["name"] = self.name
            print("Valid")
        else:
            return "Invalid!, 'NAME' should not be a number"

    def get_age(self):
        if isinstance(self.age,int):
           if self.age >= 0:
               return self.age
           else:
               return "Invalid age"
        raise ValueError ("Age must be an integer")
    def get_PIN(self):
        if isinstance(self.PIN, int):
            return("PIN obtained")
        elif self.get_PIN > 9999 or self.get_PIN < 1000:
            return("PIN must be an integer between(1000-9999)")
    def get_account_number(self,account_number):
        return account_number
       



u = User_information("Marcus",23,9088,83963573)
t = Transactions()
deposit = t.deposit(30)
t.paybills(20,"Food")
u.get_name()
print(u.account_details)

