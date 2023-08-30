##Neon number
num=int(input("enter the number"))
b=str(num)
a=num*num
result=0
while(a>0):
    rem=a%10
    result+=rem
    a=a//10
if(num==result):
    print("It is an neon number")
else:
    print("It is not an neon number")

    
    
    
    
