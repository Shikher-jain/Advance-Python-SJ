# def avg(a,b):
#     print("The average is:",(a+b)/2)
# avg(5,9)

# def avg01(*num):
#     print(type(num),type(avg01))
#     sum=0
#     for i in num: 
#         sum=sum+i
#     print("The average is:",sum/len(num))
# avg01(1,2,3,4,5,6,7,8,9,10)

# def avg02(**names):
#     print(type(names),"\n",type(avg02))
#     print("yoo", names["abcd"] , names["efgh"] , names["ijkl"])
# avg02(abcd="mnop",efgh="qrst" ,ijkl="uvwx")

# def avg03(a,b):
#     return (a+b)/2
# avg04=avg03(5,9)
# print(avg04)

# list1=[i*i for i in range(10)]
# print(list1)

# list01=[i*i for i in range(10) if i%2==0]
# print(list01)

# list02=[i*i for i in range(10) if i%2!=0]
# print(list02)

# l =[3,7,1,8,4,2,9,6,5,0]
# print(l)
# l.sort(reverse=True)
# print(l)
# l.sort()
# print(l)
# l.append(11)
# print(l)
# l.remove(4)
# print(l)
# l.pop()
# print(l)
# l.reverse()
# print(l)
# l.reverse()
# print(l.index(2),"index")
# print(l)
# print(l.count(2),"count")
# m=l
# m[0]=4
# print(l)
# print(m)
# m2=l.copy()
# print("use copy function")
# print(l)
# print(m)
# l.insert(1,9)
# print(l)
# l2=[1,2,3,4]
# m3=[9,8,9,7,6]
# l.extend(m)
# print(l)
# l.sort()
# print(l)
# print(l2+m3)
# print("set\n",set(l))

# x=int(input("Enter the value of x : "))
# match x:
#     case 1:
#         print("x is 1")
#     case 2:
#         print("x is 2")
#     case 3:
#         print("x is 3")
#     case 4:
#         print("x is 4")
#     case 5:
#         print("x is 5")
#     case 6:
#         print("x is 6")
#     case 7:
#         print("x is 7")
#     case _ if x!=8:
#         print("x =",x)
#     case _ :
#         print("x =",x)

# tuple01 = (0,1,2,3,4,5,6,7,8,9)
# tuple02 = (0,1,2,3,4,5,6,7,8,9)
# x=list(tuple01)
# t01=tuple01
# t02=tuple02
# t03=t01+t02
# print(x)
# print(list(tuple01))
# print(tuple01)
# print(tuple02)
# print(t03)
# print("'count is'",t03.count(0))
# print("'index is'",t03.index(0))
# print("'index b/w 8 & 13 is'",t03.index(0,8,13))#  kya , kaha se , kaha tak
# print("'count is'",t03.count(0))

# print("String Formatting old")
# let01="my name is {} and I'm from {}"
# let02="my name is {} and I'm from {}"
# let03="my name is {0} and I'm from {1}"
# name="Shikher"
# city="Agra"
# print("let01.format(name,city)",let01.format(name,city))
# print("let02.format(city,name)",let02.format(city,name))
# print("let03.format(name{0},city{1})",let03.format(name,city))

# print("String Formatting new by using 'f' string print(f"'""'")" )
# print(f"my name is {name} and I'm from {city}")
# print(f"my name is {{name}} and I'm from {{city}}")
# rate=78.0787
# print(f"rate is {rate:.2f}")

# print("Docstring")
# def sq(n):
#     '''This is Docstring in Python'''
#     print(n**2)
# sq(4)
# print(sq.__doc__)
# print('''>>> import this 
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!''')

# print("Set")
# s07={1,2,5,6,9,0}
# s05={1,2,5,6,9,0}
# s03={1,2,5,6,9,0}
# s05={1,2,5,6,9,0}
# s01={1,2,5,6,9,0}
# s08={3,4,7,8,1,3}
# s06={3,4,7,8,1,3}
# s04={3,4,7,8,1,3}
# s06={3,4,7,8,1,3}
# s02={3,4,7,8,1,3}
# print(s01)
# print(s02)
# print("union ",s01.union(s02))
# s03.update(s04)
# print("update",s03)
# print("intersection",s01.intersection(s02))
# s05.intersection_update(s06)
# print("intersection_update",s05)
# print("symmetric_difference ",s01.symmetric_difference(s02))
# print(s01)
# print(s02)
# print("symmetric_difference_update ",s01.symmetric_difference_update(s02))
# print("difference ",s01.difference(s02))
# print("difference_update ",s07.difference_update(s08))
# print(s01)
# print(s02)

# s01={"abc","xyz","pqr","mno","uvw"}
# s02={"cba","zyx","rqp","onm","wvu"}
# print(s01)
# print(s02)
# print("isdisjoint",s01.isdisjoint(s02))
# print("issuperset",s01.issuperset(s02))
# print("issubset",s01.issubset(s02))
# print("issubset",s01.issubset(s02))
# s01.add("ijk")
# s02.add("kji")
# print(s01)
# print(s02)
# s01.remove("ijk")
# s02.discard("kji")
# s01.pop()
# s02.pop()
# print(s01)
# print(s02)


# s01.clear()
# s02.clear()
# print(s01)
# print(s02)

# info={"sj",19,False,5.10}
# print(info)
# if "sj" in info:
#     print("sj is present")
# else:
#     print(absent)

# print("Raise custom errors")
# a=int(input("Enter no. b/w 4 and 11: "))
# if(a<4 or a>11):
#     raise ValueError("Enter b/w 4and 11")
# else:
#     print("Thanks")

# print("Dictionary in Python")
# p={}
# print("empty dictionary",p)
# print(type(p))
# p=set()
# print(type(p))
# dic={
#     "index":"user defined",
#     "name":"Shikher",
#     "mid name":" ",
#     "last name":"Jain",
#     "Roll no.":"2200020100075"
# }
# print(dic)
# print(dic["name"])
# print(dic["Roll no."])
# print(dic.get("Roll no."))
# print(dic.get("Name"))
# print(dic.get("name"))
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# print("\n")
# for key in dic.keys():
#     print(f"the value of key {key} is {dic[key]}")
# print("\n")
# for key,value in dic.items():
#     print(f"the value of key {key} is {value}")

# emp01={10:78,30:45,50:98}
# emp02={11:28,33:75,55:89}
# print(emp01)
# print(emp02)
# print(emp01.items()) 
# print(emp02.items()) 
# emp01.update({70:71})
# emp01.update({50:12})
# emp02.update({11:71})
# emp02.update({77:12})
# print("\n")
# print(emp01.items()) 
# print(emp02.items()) 
# emp02.clear()
# print(emp02.items()) 
# emp02.update({11:71})
# emp02.update({22:12})
# emp02.update({33:21})
# emp02.update({44:22})
# print(emp02.items()) 
# emp01.pop(50)
# print(emp01.items()) 
# emp01.popitem()
# print("emp01.popitem()\nPOP last item from dictionary",emp01.items()) 
# del emp02[11]
# print(emp02) 

# n=list(input("Eenter list: "))
# for i in n:
#     print(i)
# else:
#     print("Not i")
# print(n)

# n=int(input("Enter the no. of elemens in list: "))
# lists=[]
# i=int(i)
# for i in range(n):
#     x=int(input(f"Enter {i+1} element: "))
#     lists.append(x)
# print(lists)

# print("Exception Handling")
# try:
#     a=int(input("Enter the No."))
#     print(f"Multiplication table of {a} is:\n")
#     for i in range(1,11):
#         print(f"{a}*{i}={a*i}")
# except Exception as e:
#     print(Exception)
#     print(e)
# print("IMPORTANT LINES OF CODE")

# try:
#     num=int(input("Enter number: "))
#     a=[2,4,6,8]
#     print(a[num])
# except ValueError:
#     print("Not an Integer value")
# except IndexError:
#     print("Index Error")
# except MemoryError:
#     print("Memory Error")
# raise WindowsError("WINDOWSERROR")
    
# def idk(i):
#     try:
#         l=['f','i','l','l','y','n','a']
#         print(l)
#         print(l[i])
#         return 'try'
#     except:
#         print("Error")
#         return 'except'
#     finally:
#         print("Always executed")
# i=int(input("Enter index: "))
# z=idk(i)
# print(z)

# print("if-else One Line: ")
# a=int(input("Enter a = "))
# b=int(input("Enter b = "))
# ans= "a>b" if a>b else "a=b" if a==b else "a<b"
# print(ans , "By this ans= 'a>b' if a>b else 'a=b' if a==b else 'a<b'")
# print("a>b") if a>b else print("a=b") if a==b else print("a<b")
# print("^^^\nBy normal one line...")

#        00,01,02,03,04,05,06,07,08,09,10
#        || || || || || || || || || || ||
#        \/,\/,\/,\/,\/,\/,\/,\/,\/,\/,\/
# marks=[80,99,90,56,67,78,82,61,50,40,71]

# print("BY NORMAL FOR LOOP: ")
# index=0
# for mark in marks:
#     print(mark)
#     if(index==4): 
#         print("YOO0!!!")
#     index +=1

# print("-*-> ENUMERATE <-*-")
# for index,mark in enumerate(marks):
#     print("index:",index,"mark:",mark)
#     if(index==4):
#         print("YOOO!!!")

# print("-*-> ENUMERATE  start by default value <-*-")
# for index,mark in enumerate(marks,start=1):
#     print("index:",index,"mark:",mark)
#     if(index==4):
#         print("YOOO!!!")


# Different b/w "is" and "=="
# a=7
# b='7'
# c=4
# d=7
# "==" (value) and "is" (exact location of object in memory)
# print("a == b","-->",f"{a} == {b}","-->", a == b)
# print("a is b","-->",f"{a} is {b}","-->", a is b) 
# print("a == c","-->",f"{a} == {c}","-->", a == c)
# print("a is c","-->",f"{a} is {c}","-->", a is c) 
# print("a == d","-->",f"{a} == {d}","-->", a == d)
# print("a is d","-->",f"{a} is {d}","-->", a is d) 

l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
print("l1 == l2","-->",f"{l1} == {l2}","-->", l1 == l2)
print("l1 is l2","-->",f"{l1} is {l2}","-->", l1 is l2) 