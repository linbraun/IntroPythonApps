import sys
 
account_balance = float(500.25)

def printbalance(balance): # Custom function to print current balance
  print('Your current balance:')
  print(balance) # Function returning current balance

def deposit(balance): # Custom function to make deposit
  deposit_amount = float(input('How much would you like to deposit today?\n')) # Input deposit amount within the function
  balance += deposit_amount
  print('Deposit was $%.2f'%deposit_amount + ', current balance is $%.2f'%balance) # Function returning deposited amount and new balance

def withdraw(balance): # Custom function to withdraw
  withdrawal_amount = float(input('How much would you like to withdraw today?\n')) # Input withdrawal amount within the function
  if withdrawal_amount > balance:
    print('$%.2f'%withdrawal_amount + 'is greater than your account balance of $%.2f'%balance) # Function returning withdrawal amount and unchanged balance
  else:
    balance -= withdrawal_amount
    print('Withdrawal amount was $%.2f'%withdrawal_amount + ', current balance is $%.2f'%balance) # Function returning withdrawal amount and new balance
    
userchoice = input("What would you like to do?\n") # Input to choose function

if userchoice == 'B':
  printbalance(account_balance)

if userchoice == 'D':
  deposit(account_balance)
  
if userchoice == 'W':
  withdraw(account_balance)
  
if userchoice == 'Q':
  print('Thank you for banking with us.') # Exits the program

