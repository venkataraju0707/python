"""num=(1,2,3,4,5)
print("original list:",num)
result=map(lambda x:x+x+x,num)
print(list(result))

num1=[1,2,3]
num2=[4,5,6]
num3=[7,8,9]
print("original list")
print(num1,num2,num3)
result=map(lambda x,y,z:x+y+z,num1,num2,num3)
print(list(result))"""



"""color=["red","blue","black","white","pink"]
print("original list:")
print(color)
print("\nafer listify the list of strings are:")
result=list(map(list,color))
print(result)"""



"""bases=[10,20,30,40,50]
index=[1,2,3,4,5]
result=list(map(pow,bases,index))
print(result)"""



def square(n):
    return n*n
num=[1,2,3]
result=map(square,num)
print(list(result))
