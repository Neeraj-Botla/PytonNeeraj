#Write a program to print if a given number is odd or even


a=int(input('Enter a number: '))
b=a%2
if b==0:
    print(f"{a} is a Even number")
else:
    print(f"{a} is a Odd number")
