customer=[
{"name":"John","card":12345,"pin":1234,"balance":5000},
{"name":"Cathy","card":23456,"pin": 4567,"balance":10000}
]     
while True:
    print("*** HDFC ATM ***")
    z=input("existing customer (y/n) :")
    if z=='b':
        print("Exiting the ATM system.")
        break
    if z == 'n':
        c=input("would you like to open an acoount in our bank (y/n):")
        if c == 'y':
            nam=input("Enter your first name :")
            print(f" Hello {nam}")
            import random as r
            f=r.randint(10000,99999)
            l=r.randint(1000,9999)            
            print(f"your card no is {f}")
            print(f"your pin is {l}")
            print("your balance is  0")
            customer.append({"name":nam,"card":f,"pin":l,"balance":0}),
            
            cardnum=int(input("Enter your card no : "))
            passcode=int(input("Enter code : "))
            for i in  range(len(customer)):
                if cardnum==customer[i]["card"] and passcode==customer[i]["pin"]:
                    print("Welcome,", customer[i]["name"])
                    balance=customer[i]["balance"]

                    while True:
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Balance")
                        print("4. fund transfer")
                        print("5.loan")
                        print("6.Exit")
                        choice = int(input("Enter your choice: "))

                        if choice==1:
                            amount=int(input("Enter Amount: "))
                            balance=balance+amount
                            customer[i]["balance"]=balance
                            print("You current balance is ",balance)
                        elif choice==2:
                            amount=int(input("Enter Amount : "))
                            if balance<amount:
                                    print("Insufficient Balance")
                            else:
                                balance=balance-amount
                                customer[i]["balance"]=balance
                                print("You current balance is ",balance)
                        elif choice==3:
                            print("You current balance is ",balance)
                        elif choice == 4:
                            fundcard=int(input("enter the bank holder act no to which you want to transfer :"))
                            print(f" your balane is {balance}")
                            for p in range(len(customer)):
                                if fundcard==customer[p]["card"]:
                                    print("The account is on the name ", customer[p]["name"])
                                    break
                            transamount=int(input("enter the amount you want to transfer : "))
                            if customer[i]["balance"]>=transamount:
                                h=customer[i]["balance"]-transamount
                                customer[i]["balance"]=h
                                r=customer[p]["balance"]+transamount
                                customer[p]["balance"]=r
                                print(f"Amount of {transamount} is transferd to ",customer[p]["name"])
                                print(" your balance is ",customer[i]["balance"])
                            else:
                                print("insufucient funds")
                        elif choice == 6:  # Exit transaction menu
                                print("Exiting.")
                                break     
                        elif choice!=1 and choice!=2 and choice!=3 and choice!=4 and choice!=5 and choice!=6:
                
                            print("Invalid Inpuy")
                        elif choice==5:
                            loanamt=int(input("enter amount you want to take : "))
                            balance=balance+loanamt
                            customer[i]["balance"]=balance
                            
        
   
    else:
        cardnum=int(input("Enter your card no : "))
        passcode=int(input("Enter code : "))
        for i in  range(len(customer)):
            if cardnum==customer[i]["card"] and passcode==customer[i]["pin"]:
                print("Welcome,", customer[i]["name"])
                balance=customer[i]["balance"]
                print(f" your balance is {balance}")

                while True:
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Balance")
                    print("4. fund transfer")
                    print("5.loan")
                    print("6.Exit")
                    
                    choice = int(input("Enter your choice: "))
                    if choice==1:
                        amount=int(input("Enter Amount: "))
                        balance=balance+amount
                        customer[i]["balance"]=balance
                        print("You current balance is ",balance)
                    elif choice==2:
                        amount=int(input("Enter Amount : "))
                        if balance<amount:
                                print("Insufficient Balance")
                        else:
                            balance=balance-amount
                            customer[i]["balance"]=balance
                            print("You current balance is ",balance)
                    elif choice==3:
                        print("You current balance is ",balance)
                    elif choice == 4:
                        fundcard=int(input("enter the bank holder act no to which you want to transfer :"))

                        for p in range(len(customer)):
                            if fundcard==customer[p]["card"]:
                                print("The account is on the name ", customer[p]["name"])
                                break
                        transamount=int(input("enter the amount you want to transfer : "))
                        if customer[i]["balance"]>=transamount:
                            h=customer[i]["balance"]-transamount
                            customer[i]["balance"]=h
                        
                            r=customer[p]["balance"]+transamount
                            customer[p]["balance"]=r
                            print(f"Amount of {transamount} is transferd to ",customer[p]["name"])
                            print(f" your balance is ",customer[i]["balance"])
                        else:
                            print("insufucient funds")
                    
                    elif choice == 6:  # Exit transaction menu
                        print("Exiting.")
                        break
                    

                    elif choice!=1 and choice!=2 and choice!=3 and choice!=4 and choice!=5 and choice!=6:
                        print("Invalid Input")
                    elif choice==5:
                        loanamt=int(input("enter amount you want to take : "))
                        balance=balance+loanamt
                        customer[i]["balance"]=balance
                   