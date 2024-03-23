"variables access"

"""class student:
    college="GVPT"
    def __init__(self,name,m1,m2):
        self.name=name
        self.m1=m1
        self.m2=m2
    def result(self):
        
        print(" {name} got {m1} marks in math1".format(name=self.name,m1=self.m1))
        
s1=student("msdhoni",25,25)
s2=student("virat",20,20)
print(s1.m1,s1.m2,s1.college)
s1.result()
s2.result()"""




"""METHOD ACCESS
class student:
    college="GVPT"

    @classmethod
    def standard(cls):
        print("class method is executed")
    def __init__(self,name,m1,m2):
        self.name=name
        self.m1=m1
        self.m2=m2
    def result(self):
        
        print(" {name} got {m1} marks in math1".format(name=self.name,m1=self.m1))
    @staticmethod
    def rank():
       return "rank"
s1=student("msdhoni",24,24)
s2=student("virat",25,25)
s1.standard()"""
#INNER CLASS
"""class student:
    def __init__(self,name):
        self.name=name
        self.c1=self.children()
    def show(self):
        print(self.name)
        
    class children:
         def __init__(self):
             self.name="ms"
         
s1=student("msd")
s1.show()
#s1.c1.children()
print(s1.c1.name)"""


"""class vehicles:
    def __init__(self,name):
        self.name=name
        
    def speed(self):
        print("{name}is vehicle".format(name=self.name))
class bike:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("{n} is bike".format(n=name))
class cycle(vehicles,bike):
    def __init__(self,name):
        self.name=name
    def show(self):
        print("this is cycle")
    
#b=bike("yamaha")
c=cycle("yamaha")
#b.speed()
#b.show()
c.show()"""

    
class vehicles:
    def __init__(self,name):
        self.name="ms"
        
    def speed(self):
        print("{name}is vehicle".format(name=self.name))
class bike(vehicles):
    def __init__(self,name):
        super.__init__()
        self.name="msd"
    def speed1(self):
        print("{name}is vehicle".format(name=self.name))

b=bike()

























   
