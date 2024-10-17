customer=[{"name":"John","card":12345,"pin":1234,"balance":5000}]


print("*** HDFC ATM ***")


while True:
    
    
    cardnum=int(input("Enter your card no : "))
    passcode=int(input("Enter code : "))
    



    if cardnum== customer[0]["card"] and passcode == customer[0]["pin"]:
        print("Welcome,", customer[0]["name"])
        balance=customer[0]["balance"]
        print(f" your balane is {balance}")
    



        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            if choice==1:
                amount=int(input("Enter Amount: "))
                balance=balance+amount
                print("You current balance is ",balance)
            elif choice==2:
                amount=int(input("Enter Amount : "))
                if balance<amount:
                    print("Insufficient Balance")
                else:
                    balance=balance-amount
                    print("You current balance is ",balance)
            elif choice==3:
                print("You current balance is ",balance)
            elif choice==4:
                break
            else:
                print("Invalid Input")
    else:
        print("invald input")
        