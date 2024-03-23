import re
s=input()
k=input()
m=re.search(r"k", s)
print(m.start())
print(m.end())
