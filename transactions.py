
class Transactions:
    def __init__(self):
        self.balance = 0
        self.transaction = []
        
    def deposit(self,amount: float):
        if amount > 0:
            self.balance += amount 
            self.transaction.append(f"${amount} deposited")
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
            self.transaction.append(f"${amount} withdrawed")
            return f"${amount} withdrawn\nCurrent balance is ${self.balance}"
        
    def transfer_money(self,sender: str,amount: float,receiver: str):
        if amount <= self.balance:
            self.balance = self.balance - amount
            self.transaction.append(f"${amount} transfered")
            return( f"Transfer to {receiver} successful! current balance is ${self.balance}")
        elif amount > self.balance:
            return( f"You can't transfer ${amount}, your balance is ${self.balance}")

    def view_balance(self):
        print( f"Balance: ${self.balance}")
    
    def paybills(self,amount: float,bill: str):
        if amount < self.balance :
            self.balance -= amount
            self.transaction.append(f"${amount} for {bill} payment")
            print( f"${amount} {bill} paid successfully!" )
            return self.view_balance()
        elif amount < 0 or amount > self.balance:
            print("Invalid amount/Insufficient balance")






t = Transactions()
deposit = t.deposit(30)



