
class BankAccount:
    accounts =[]
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self,amount):
        self.balance += amount 
        return self 

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount 
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        return f"{self.balance}"
    
    def yield_interest(self):
        self.balance >= 0 
        self.balance += (self.balance * self.int_rate)
        return self 

    @classmethod
    def show_bank_info(cls):
        for account in cls.accounts:
            account.display_account_info()   

class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(.2, 500),
            "savings" : BankAccount(.5, 1000)
        }

    
    def display_user_balance(self):
        print(f"User: {self.name} --- Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name} --- Savings Balance: {self.account['savings'].display_account_info()} ")
        return self 
        

    def transfer_money(self,other_user,amount):
        self.user_balance -= amount 
        other_user.user_balance += amount 
        self.display_user_balance()
        other_user.display_user_balance()


nina = User("Nina Ramirez")
nina.account['checking'].deposit(2000).withdraw(200).deposit(40).withdraw(600)
nina.account['savings'].deposit(3000)
nina.display_user_balance()
