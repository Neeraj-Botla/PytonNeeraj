#
"""while True:
    # Input from the user
    number = input("Enter a number (or 'stop' to quit): ")
    
    if number.lower() == 'stop':
        break
    
    try:
        number = int(number)
        
        # Check if the number is prime
        if number < 2:
            print(f"{number} is not a prime number.")
        else:
            for i in range(2, number):
                if number % i == 0:
                    print(f"{number} is not a prime number.")
                    break
            else:
                print(f"{number} is a prime number.")
    except ValueError:
        print("Please enter a valid integer.")"""

a=("hello")
print ("hello" in a)
