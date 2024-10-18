n = int(input("Enter your number: "))
for i in range(2, n):
    if n % i == 0:
        print("It is not a prime number.")
        break
else:
    print("Your number is prime.")

    
    
