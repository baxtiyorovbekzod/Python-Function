def menyu():
    print("""
          1.Balans tekshirish.
          2.Balansga pul solish.
          3.Balansdan pul yechish.
          0.orqaga qaytish.
          """ )
def  deposit(balance, amount):
    if amount>0:
        balance+=amount
    return balance
def withdraw(balance, amount):
    if balance>=amount:
        balance-=amount      
    return balance 
def check_balance(balance):
        print(f"Sizning balansingiz {balance}")
def main(): 
    balance=50000.00
    while True:
        menyu()
        choice=input(">")
        if choice=="1":
             check_balance(balance)
        elif choice=="2":
            amount=float(input("Sum:"))
            balance=deposit(balance, amount)
        elif choice=="3":
             amount=float(input("Sum:"))
             balance=withdraw(balance, amount)
        elif choice=="0":
             break
        else:
             print("Bunday menyu yo'q") 
main()                     
