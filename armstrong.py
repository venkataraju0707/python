"""n=int(input("enter the number:"))
#list1=[]
#list1.append(n)
#print(list1)
str1=str(n)
print(len(str1))
print(n[:1])
#print(2**3)"""
n=int(input("enter the number:"))
l=len(str(n))
sum=0
temp=n
while temp>0:
    
    digit=temp%10
    sum+=digit**l
    temp//=10
#sum=0
#for i in l:
 #   sum+=i**
    
if sum==n:
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")
"""# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")"""

        
    
