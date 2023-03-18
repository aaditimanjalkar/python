# Write a python program to create a bank class where deposits and withdrawal can be handled by using instance methods.
import random
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Vidyalankar Bank pvt. ltd.")
        
    def createacc(self):
      name=input("Enter name (in lower case): ")
      pin=int(input("Enter Pin: "))
      a=random.randint(1000000, 9999999)
      b=0
      c=[]
      bank[a]=[name,pin,b,c]
      print("Name: ",name,"\nAccount no.: ",a,"\nPin: ",pin)
      
    def login(self,account_number):
       if account_number not in bank:
          print("Account not found!")
          return False
       else:
          print("Welcome,", bank[account_number][0])
          return True
          
    def deposit(self,account_number):
        a1=account_number
        if a1 in bank:
           amount=float(input("Enter amount to be Deposited: "))
           pin=int(input("Enter Pin: "))
           if pin==bank[a1][1]:
            self.balance += amount
            bank[a1][2]=self.balance
            print("Amount Deposited: ",amount)
            bank[a1][3].append("Deposited:")
            bank[a1][3].append(amount)
           else:
             print("Enter PIN is wrong")
           

    def withdraw(self,account_number):
        a1=account_number
        if a1 in bank:
         amount = float(input("Enter amount to be Withdrawn: "))
         if self.balance>=amount:
           pin=int(input("Enter Pin: "))
           if pin==bank[a1][1]:
            self.balance-=amount
            bank[a1][2]=self.balance
            print("You Withdrew: ", amount)
            bank[a1][3].append("Withdrew:")
            bank[a1][3].append(amount)
         else:
            print("Sorry!Unable to withdraw money due to Insufficient balance!!!")
        
    def display(self,account_number):
      a1=account_number
      if a1 in bank:
        pin=int(input("Enter Pin: "))
        if pin==bank[a1][1]:
          print("Net Available Balance: ",bank[a1][2])

    def trans(self,account_number):
       a1=account_number
       if a1 in bank:
        pin=int(input("Enter PIN:"))
        if pin==bank[a1][1]:
          print("Your transaction history is:")
        for i in bank[a1][3]:
          print(i)
        else:
          print("Incorrect PIN!!")
       else:
        print("Invalid account number!!")   
print("Hello!!! Welcome to the Vidyalankar Bank pvt. ltd.")
s = Bank_Account()
bank={}
while 1:  
  ch=int(input("MENU\n1.Create Account\n2.Login\n3.Exit\nEnter a choice: "))
  if ch==1:
    s.createacc()
  elif ch==2:
    account_number = int(input("Enter your account number: "))
    s.login(account_number)
    while 1:
      ch=int(input("1.Deposit money\n2.Withdraw money\n3.View Balance\n4.Transation History\n5.Exit\nEnter a choice: "))
      if ch==1:
        s.deposit(account_number)
      elif ch==2:
        s.withdraw(account_number)
      elif ch==3:
        s.display(account_number)
      elif ch==4:
        s.trans(account_number)
      elif ch==5:
        break
      else:
        print("Invalid choice!!")
  elif ch==3:
      print("Thank You...!! Visit again...!!")
      break
  else:
      print("Invalid choice!!")
