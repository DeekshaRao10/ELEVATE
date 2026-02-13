
class BankAccount:
    

    def __init__(self, account_holder, balance=0):
        
        self.account_holder = account_holder  
        self.__balance = balance              
    def get_balance(self):
       
        return self.__balance

    
    def deposit(self, amount):
       
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    
    def withdraw(self, amount):
       
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

  
    def display(self):
        """Displays account information."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.__balance}")



class SavingsAccount(BankAccount):
    """Represents a savings account with interest."""

    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        """Constructor using inheritance."""
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    
    def display(self):
        """Overrides display method to include interest rate."""
        super().display()
        print(f"Interest Rate: {self.interest_rate * 100}%")



if __name__ == "__main__":

    
    account1 = BankAccount("Afshan", 1000)
    account2 = SavingsAccount("Deeksha", 2000, 0.07)

    
    print("\n--- Account 1 Operations ---")
    account1.deposit(500)
    account1.withdraw(300)
    account1.display()

    print("\n--- Account 2 Operations (Savings) ---")
    account2.deposit(1000)
    account2.withdraw(2500)  
    account2.display()

    print("\nFinal Balance Account 1:", account1.get_balance())
    print("Final Balance Account 2:", account2.get_balance())
