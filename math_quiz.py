import random as r
print("** Math Quiz ***")
score=0
i=1
while i<=5:
    
    a = r.randint(1,9)
    b = r.randint(1,9)
    print(f"{i}.{a}+{b}=")
    ans=int(input("enter your ans : "))
    j=0
    while j==0:
        
        
        answer=a+b
        if ans==a+b:
            print("corret")
            score +=1
        
           
            

            break
        
    
        else:
            print("wrong ans")
            print(f"correct aneswer is {answer} ")
            
            break
    i=i+1   
print(f"your total score is {score}/5")    
   