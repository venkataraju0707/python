n=int(input("enter the numbers:"))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit
    temp=temp//10
print(sum)    

if n%sum==0:
    print("given number is hasrshad number")
else:
    print("given number  is not harshad number")
