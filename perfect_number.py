num=int(input("enter the number:"))
sum=0
sum1=0
for i in range(1,num):
    if num%i==0:
        sum+=i
        print(sum)
    sum1+=0    
        
if sum==num:
    print("your number is perfect number")
else:
    print("your number is not perfect number")
    
    
