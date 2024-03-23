 
    
"""num = int(input("Enter the number: "))  
list1 = [] #an empty list  
for i in range(num):
  list1.append([])  
  list1[i].append(1)  
  for j in range(1, i):  
    list1[i].append(list1[i-1][j-1] + list1[i-1][j])  
  if(num != 0):  
    list1[i].append(1)
    for i in range(num):  
  print(" " * (num - i), end = " ", sep = " ")  
  for j in range(0, i + 1):  
    print('{0:6}'.format(list1[i][j]), end = " ", sep = " ") 
print(list1)"""


"""num=int(input("enter the number"))
list1 = []
for i in range(0,num):
    list1.append([])
    list1[i].append(1)
    for j in range(1,i):
        list[i].append(list1[i-1][j-1]+list1[i-1][j])
    if(num !=0):
        list1[i].append(1)
print(list1)"""
            
num = int(input("Enter the number: "))  
list1 = [] 
for i in range(num):
  list1.append([])  
  list1[i].append(1)  
  for j in range(1, i):  
    list1[i].append(list1[i-1][j-1] + list1[i-1][j])  
  if(num != 0):  
    list1[i].append(1)
  #print("  "*(num-i),end="",sep= " ")
print("\n",join(list1))  
"""for j in range(0,i+1):
    print('{0:6}'.format(list1[i][j],end="",sep="")
print(list1) """         
"""n = int(input("Enter the number of rows:"))  
list=[]
# iterarte upto n  
for i in range(n):
  list.append("*"*i)
print("\n".join(list))"""

  





























