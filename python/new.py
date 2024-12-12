x=["1","hi","!","by","6",".git"]
print("Before sort",x)
x.sort()
print("After sort",x)

'''

O/P:-
x=["!",".git","1","6","by","hi"]

'''
def f2():
    print("f2 is",x)
    
def f1():
    x=[1,2,3,4,5,6,7,8,9,0]
    print("f1 is",x)
    f2()
f1()
f1()
def f4():
    print("f4 is",x)
    
def f3():
    global x
    x=[1,2,3,4,5,6,7,8,9,0]
    print("f3 is",x)
    f4()
f3()
f3()


# Arguments
def Arguments(argument,new):
    print(argument,new," Element:")
for no in range(1,6,1):
    no=str(no)
    z=input("Enter "+no+" Element :")
    Arguments(z,no)