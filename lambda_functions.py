"""r=lambda a:a+15
print(r(8))
r=lambda c,f: c*f
print(r(3,4))








def func(n):
    return lambda a:a*n

result=func(2)
print(result(15))"""


subject=[("english",99),("science",94),("maths",87),("telugu",59)]
print("original list of tuples:")
subject.sort(key=lambda x:x[1])
print("\n sorting the lsit of tuples:")
print(subject)
