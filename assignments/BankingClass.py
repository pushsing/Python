import random
class Bank:
    'Contains customer details including balance'
    numberofcustomers = 0
    cstmr=[]

    def __init__(self, name, balance):
        self.name = name
        self.balance= balance
        self.accountnumber=random.randint(1000,9999)
        print("Account successfully created : Name- ",self.name," Balance- ",self.balance, " Account Number- ", self.accountnumber)
        Bank.numberofcustomers += 1

    def deposit(self,deposit):
        self.balance=self.balance+deposit
        print("Deposit done. Current balance: "+str(self.balance))
    def withdrawl(self,withdrawl):
        self.balance=self.balance-withdrawl
        print("Withdrawl done. Current balance: ",self.balance)
print("For creating a bank account press: c")
x=input()
if x=='c':
    print("Enter name:")
    n=input()
    print("Enter starting amount:")
    a=int(input())
    c = Bank(n,a)
    Bank.cstmr=Bank.cstmr+[c]
else:
    print("Wrong input")
    exit()
print("For deposit press : d")
print("For withdrawl press: w")
x=input()
if x=='w':
    n=int(input("Enter account number: "))
    j=0
    flag=0
    for i in Bank.cstmr:
        if Bank.cstmr[j].accountnumber==n:
            flag = 1
            z=int(input("Enter withdrawl amount:"))
            if z>Bank.cstmr[j].balance:
                print("Amount cannot be dispensed")
                exit()
            else:
                Bank.cstmr[j].withdrawl(z)
                exit()
        j=j+1
    if(flag==0):
        print("Wrong account number")
elif x=='d':
    n = int(input("Enter account number: "))
    j = 0
    flag = 0
    for i in Bank.cstmr:
        if Bank.cstmr[j].accountnumber == n:
            flag = 1
            z = int(input("Enter deposit amount:"))
            Bank.cstmr[j].deposit(z)
            exit()
        j = j + 1
    if (flag == 0):
        print("Wrong account number")
else:
    print("Wrong input")
    exit()