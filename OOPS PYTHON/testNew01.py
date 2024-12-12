# same name of class and funciion is allowed
class person:
    def test(self):
        print("TEST 1")    
class test:
    def test():
        print("TEST 2")

b=person()
print(b)
b.test()
# print(b.person())
cname=input("Enter The Class Name:g ") #in a string form
cName=globals()[cname]
x=cName()
x.test()
print(x)

