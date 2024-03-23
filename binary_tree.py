"""class BinaryNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data==self.data:
                return
        if data<self.data:
            if self.left:
                self.left.add_child(data)

            else:
                self.left=BinaryNode(data)
        if data>self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinaryNode(data)
       
       
    def in_order_traversal(self):
        ele=[]
        if self.left:
            ele+=self.left.in_order_traversal()
        ele.append(self.data)
        if self.right:
            ele+=self.right.in_order_traversal()
             
        return ele
    def search(self,val):
        if self.data==val:
            return True
        if self.data>val:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if self.data<val:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.max_ele()
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.min_ele()
    
        
    
            
def root(ele):
    root=BinaryNode(ele[0])
    for i in range(1,len(ele)):
        root.add_child(ele[i])
    return root    
if __name__=="__main__":
    lis=[ 45, 15, 79, 90, 10, 55, 12, 20, 50]
    ilr=root(lis)
    print(ilr.in_order_traversal())
    print(ilr.search(8))"""
    






class BinaryNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
       if self.data==data:
           return
       if self.data<data:
           if self.left:
               self.left.add_child(data)
           else:
               self.left=BinaryNode(data)
       if self.data>data:
           if self.right:
               self.right.add_child(data)
           else:
               self.right=BinaryNode(data)        
        
    def in_order_traversal(self):
        ele=[]
        if self.left:
            ele+=self.left.in_order_traversal()
        ele.append(self.data)
        if self.right:
            ele+=self.right.in_order_traversal()
        return ele
    def search(self,data):
        if self.data==data:
            return True
        if self.data>data:
            if self.right:
                return self.right.search(data)
            else:
                return False
        if self.data<data:
            if self.left:
                return self.left.search(data)
            else:
                return False
    def find_max(self):
        if self.right:
            return self.right()
    
            
def root(ele):
    root=BinaryNode(ele[0])
    for i in range(1,len(ele)):
        root.add_child(ele[i])
    return root
if __name__=="__main__":
    lis=[ 45, 15, 79, 90, 10, 55, 12, 20, 50]
    ilr=root(lis)
    print(ilr.in_order_traversal())
    print(ilr.search(12))
    




































         
