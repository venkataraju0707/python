s=input("string")
k=input("string1")

n=len(k)
v=n
l=[]
for i in range(len(s)):
    l.append(s[i:v])
    if l[i]==k:
        print((i,v-1))
    i=v
    v=v+n-1
