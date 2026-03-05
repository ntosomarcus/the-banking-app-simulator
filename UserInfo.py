from transactions import Transactions

class User_information(Transactions):
    def __init__(self,name: str,age: int,PIN: int, account_num):
        self.name = name 
        self.age = age
        self.PIN = PIN
        self.account_details = {
            self.name: {"transaction": [], 
                        "PIN": self.PIN}
                                }
    def get_name(self):
        if isinstance(self.name,str):
            return self.name
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
            return self.PIN
        elif self.get_PIN > 9999 or self.get_PIN < 1000:
            return("PIN must be an integer between(1000-9999)")
    def get_account_number(self,account_number):
        return account_number
       
u = User_information("Ben",23,3039,293990293343343)
name = u.get_name()
print(u.account_details)
