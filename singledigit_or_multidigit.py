# Accept a number and print if it is a single digit or multi digit number


Number=int(input('enter the value of Number: '))
if Number<10:
    print(f"{Number} is single digit")
if Number>=10:
    print(f"{Number} is multi digit")