class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number 
    self.__account_holder_name = account_holder_name 
    self.__account_balance = initial_balance 
    
    def deposit(self, amount): 
      if amount > 0: 
       self.__account_balance += amount return f"Deposited ${amount}.
       New balance: ${self.__account_balance}"
      else:
        return "Invalid deposit amount."
        
        def withdraw(self, amount):
          if 0 < amount <=
          self.__account_balance:
            self.__account_balance -= amount 
            return f"Withdrew ${amount}. New balance: ${self.__account_balance}" 
          else:
            return "Insufficient funds or invalid withdrawal amount."
            
            def display_balance(self): 
              return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}" 
              
  # Create an instance of BankAccount account=BankAccount account("123456","John Doe",1000.0)

  #Test deposit and withdrawal
  print(account.display_balance())
  print(account.deposit_balance(500.0))
  print(account.withdraw_balance(200.0))
  print(account.display_balance())
