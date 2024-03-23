n=int(input("enter the number:"))
temp=n
sum=0
def fact(digit):
    s=1
    if digit==0:
        return 1
    for i in range(1,digit+1):
        s*=i
    print(s)
    return s
while temp>0:
    digit=temp%10
    f=fact(digit)
    sum+=f
    temp=temp//10
if sum==n:
    print("your number is strong")
else:
    print("your number is not strong")
    
print(fact)    
print(sum)
