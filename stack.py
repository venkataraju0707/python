class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None
    def add_val(self,data):
        node=Node(data,self.head)
        self.head=node
    def add_at_ending(self,data):
        if self.head is None:
            self.head=Node(data,None)
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next==Node(data,None)    
        
    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr=self.head
        l=""
        while itr:
            l+=str(itr.data)+"->"
            itr=itr.next
        print(l)   
l=linkedlist()
l.add_val(1)
l.add_val(2)
l.add_val(3)
l.add_val(4)
l.add_val(5)
l.add_val(6)
l.add_at_ending(-1)
l.add_at_ending(0)
l.print()
        
        
