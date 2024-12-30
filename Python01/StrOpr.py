s="geeks"
k=[(i.upper(),len(i)) for i in s]
print(k)

print([(i.lower()) for i in "GFG"])

s1=["geeks","for","geeks"]
print([(i.lower(),len(i)) for i in s1])

# t=32.00
t=[1,2,3,4,5,6,7,8,9,0]
d=[round((x-32)*5/9)for x in t]
print(d)