# Accept year of joining, salary and print bonus(5%) if more than 5 years are completed


year=int(input("Enter your year of joining: "))
Salary=int(input("Enter your salary: "))
b=Salary*0.05
if year<=2019:
    print(f"{b} is your Bonus")
else:
    print('Bonus not available')
