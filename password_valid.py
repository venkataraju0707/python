#def oddStream(n, base=3):
 #   if n == 0:
  #  print(base)
   # return oddStream(n-1, base=base+2)

#def evenStream(n, base=0):
 #   if n == 0:
  #      return
   # print(base)
    #return oddStream(n-1, base=base+2)

#def print_from_stream(n, stream):
 #   if stream == 'even':
  #      return evenStream(n)
   # elif stream == 'odd':
    #    return oddStream(n)

#number_of_lines = int(input())

#for _ in range(number_of_lines):
 #   line = input().split()
  #  stream, n = line[0], int(line[1])
   # print_from_stream(n, stream)

#def Male(name):
 #   print(name," is a male")
#def Female(name):
 #   print(name,"is female")




   
#def Gender(name,gender):
 #   if gender=="male":
  #      return Male(name)
   # else:
    #    #gender=="female":
     #   return Female(name)
        
#number_of_names=input()#When you are not interested in some values returned by a function we use underscore in place of variable name . Basically it means you are not interested in how many times the loop is run till now just that it should run some specific number of times overall.
#for _ in (number_of_names):
 #   line=input().split()
  #  name,gender=line[0],line[1]
#Gender(name,gender)

#def final_value(a,b):
 #   add(a,b)
  #  sub(a,b)
#def add(a,b):
 #   print(a+b)
#def sub(a,b):
 #   print(a-b)
#final_value(2,3)        
"""import re        
email=(input())
pattern=(r"[a-zA-Z0-9]+[@][a-z]+ [\.][a-z]{0-3}")
if re.search(pattern,email):
    print("email is valid")
else:
    print("email is valid")"""



"""import re  
def validate_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        return False  
  
email = "example@domain.com"  
if validate_email(email):  
    print("Valid email address")  
else:  
    print("Invalid email address") """
"""import re
x="venkataraju"
x1=re.search("raju",x)
print(x1)"""
         
"""import re
def email(id=input()):
    pattern=("[a-bA-B0-9]+[@][a-z]+[\.][a-z]{3}")
    if re.search(pattern,id):
        return "email is valid"
    else:
        return "email is not valid"

print(email())"""
"""y=lambda x:x+x
print(y(9))"""

n=int(input())      
for i in range(1,n):
    print(i)






































































    
