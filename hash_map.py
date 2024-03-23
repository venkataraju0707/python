"""class Hashtable:
    def __init__(self):
        self.max=10
        self.arr=[None for  i in range(self.max)]
    def get_location(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.max
    
    def add_values(self,key,values):
        h= self.get_location(key)
        self.arr[h]=values
        
    def get_values(self,key):
        h=self.get_location(key)
        return self.arr[h]

    #def __setitem__(self,key,values):
     #   h=self.get_location(key)
     #   return self.arr[h]
        


    def remove(self,key):
        h=get_location(key)
        arr[h]=None
        
h1=Hashtable()
h1.get_location("abhi")
h1.get_location("manikanta")
h1.add_values("march 5",2)
#(h1.add_values("march 6",3))
h1.add_values("march 7",4)
h1.add_values("march 8",8)
h1.add_values("march 9",12)
h1.add_values("march 15",22)
h1.add_values("march 25",32)
print(h1.get_values("march 7"))
print(h1.arr)"""

class Hashtable:
    def __init__(self):
        self.max=10
        self.arr=[None for i in range(self.max)]
    def hash_values(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.max    
    def set_values(self,key,value):
        h=self.hash_values(key)
        self.arr[h]=value
        return self.arr
    def get_values(self,key):
        h=self.hash_values(key)
        return self.arr[h]
val=Hashtable()
val.hash_values("march 6")
val.set_values("march 6",120)
val.get_values("march 6")
print(val.arr)













































