from tempClass import Employee

e1=Employee("Shikher")
print(str(e1))   
print(repr(e1))
print(len(e1))
print(e1.__str__()) 
print(e1.__repr__()) 
print(e1.__len__()) 
# print(e1.name)
e1("abcd")
e1()