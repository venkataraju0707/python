class Treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_elements(self,child):
        child.parent=self
        self.children.append(child)

def build_product_tree():
    root=Treenode("Electronics")
    laptop=Treenode("Laptop")
    laptop.add_elements(Treenode("mac"))
    laptop.add_elements(Treenode("iphone"))
    laptop.add_elements(Treenode("thinkpad"))
        
    return root

        
if __name__=="__main__":
    root=build_product_tree()
    print(root)   
