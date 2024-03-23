#n=int(input())
#for i in range(n):
 #   for j in range(i+1,n):
  #      print("*",end="")
   # print()   
num = int(input("Enter the number: "))  
list1 = [] #an empty list  
for i in range(num):  
  list1.append([])  
  list1[i].append(1)  
  for j in range(1, i):  
    list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])  
  if(num != 0):  
    list1[i].append(1)  
for i in range(num):  
  print(" " * (num - i), end = " ", sep = " ")  
  for j in range(0, i + 1):  
    print('{0:6}'.format(list1[i][j]), end = " ", sep = " ")  
  print()
  
