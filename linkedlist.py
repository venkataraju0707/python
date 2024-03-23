"""class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            print("linkedlist is empty")
            return
        itr=self.head   
        lis=""
        
        while itr:
            lis+=str(itr.data)+"->"
            itr=itr.next
        print(lis)
if __name__=="__main__":
    l=linkedlist()
    l.insert_at_begining(5)
    l.insert_at_begining(12)
    l.print()"""
            




class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            print("linked list is empty")
        itr=self.head
        lis=""
        while itr:
            lis+=str(itr.data)+"->"
            itr=itr.next
        print(lis)
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)

        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        print(count)    
    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
    def remove_at_index(self,index):
        count=0
        itr=self.head
        
        while itr:
            if count==itr:
                itr.next=itr.next.next
            count+=1
        print(self.print())    
            
        
             
             

if __name__=="__main__":
    l=linkedlist()
    l.insert_at_begining(1)
    l.insert_at_begining(2)
    l.insert_at_begining(3)
    l.insert_at_begining(4)
    l.insert_at_begining(5)
    
    l.insert_at_end(3)
    l.insert_at_end(5)
    l.insert_at_end(7)
    l.print()
    l.length()
    l.remove_at_index(7)









































        











































