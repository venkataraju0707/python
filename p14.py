"""from datetime import date
class Person:
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_birth
    def calculate_age(self):
        today=date.today()
        age=today.year-self.date_of_birth.year
        if today<date(today.year,self.date_of_birth.month,self.date_of_birth.day):
            age-=1
        return age
person1=Person("Ravi","India",date(2004,4,4))
print(person1. name)
print(person1. country)
print(person1.calculate_age)"""
                   
list=[1,2,3,4,56]
n=int(input())
pos=0
def search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos']=i
            return True
    
    
if search(list,n):
    print("found",pos)
else:
    print("not found")
