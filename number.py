n=int(input())
n1=int(input())
n2=int(input())
#num=n1+n2
num=0
count=1
while count<=n:
    print(n2,end=" ")
    num=n1+n2
    count+=1
    n1,n2=n2,num
    print(n2,end=" ")
    
