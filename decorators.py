#identity=lambda n,a:n+a
#print(identity(3,19))
#double=lambda x:x*3
#print(double(3))
#msdhoni=lambda x,y,z:x<y<z
#print(msdhoni(5,6,7))
#div=lambda x,y:x/y
#print(div(2,4))
#def div(a,b):
 #   print(a*b)
#div(2,3)
#div(5,6)
#div(5,3)
#div(4,9) 
#def div(a,b):
 #   print(a+b)
#div(2,3)
#mul=div
#print(mul(2,3))
#def ms(txt):
 #   return txt.upper()
#def dhoni(txt):
 #   return txt.lower()
#def vera(func): 
 #   print(func("hii nanna"))

#vera(ms)    
#vera(dhoni)
def login_required(f1):
    def inner(name,is_login):
        if is_login ==False:
            return
        return f1(name,is_login)
    return inner
@login_required
def home(name,is_login):
    #if is_login==True:
        print("welcome to home page our website")
    #else:
     #   print("pls kindly login")
@login_required
def orders(name,is_login):
    print("welcome to orders page of our website")
orders("venky",True)
home("venky",False)
