# Accept marks of Math, Science, English, social and print grade A, B or C based on following:
# Grade A > Percentage > 80%
# Grade B > Percentage >=60% and <80%
# Grade C > Percentage < 60%


print('Please enter your marks\nNote the total marks are For 100')
a=int(input("Marks obtained in Math: "))
b=int(input("Marks obtained in English: "))
c=int(input("marks obtained in science: "))
d=int(input("marks obtained in social: "))
T=(a+b+c+d)
print(f"{T} is your Total Marks")
if T>320:
    print("A grade")
if 320>T>240:
    print("B Grade")
if T<240:
    print('C Grade')
