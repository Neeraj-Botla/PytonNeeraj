customer=[
{"name":"John","card":12345,"pin":1234,"balance":5000},
{"name":"Cathy","card":23456,"pin": 4567,"balance":10000}
]     
while True:
    print("*** HDFC ATM ***")
    z=input("existing customer (y/n) :")


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
            while True:
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Balance")
                    print("4. Exit")
                    balance=0


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
                        print("exited")
                        break
                    

                    else:
                        print("Invalid Input")

    elif z == 'f':  # To exit the program
        print("Thank you for using HDFC ATM!")
        break


    elif z =='y':
        pass

        
            
            
        cardnum=int(input("Enter your card no : "))
        passcode=int(input("Enter code : "))
        

        for i in  range(len(customer)):
            if cardnum== customer[i]["card"] and passcode == customer[i]["pin"]:
                print("Welcome,", customer[i]["name"])
                balance=customer[i]["balance"]
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
                        print("exited")
                        break
                    

                    else:
                        print("Invalid Input")
            else:
                print("invald input")