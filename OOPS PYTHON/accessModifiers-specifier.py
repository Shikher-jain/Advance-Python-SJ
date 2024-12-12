# PUBLIC ACCESS SPECIFIER 
class Employee01:
    def __init__(self):
        self.name="Shikher"   #PUBLIC VARIABLES
        self.work="Developer 01"  #PUBLIC VARIABLES

a=Employee01()
a.emp1=66
print(a.name,a.work)

# PRIVATE ACCESS SPECIFIER 
class Employee02:
    def __init__(self):
        self.__name="Shikher"   #IDENTIFICATION OF PRIVATE VARIABLES is "__"
        self.__work="Developer 02"  #IDENTIFICATION OF PRIVATE VARIABLES is "__"

a=Employee02()
a.emp1=66
# print(a.__name,a.__work) #SHOW AN ERROR
print(a._Employee02__name,a._Employee02__work) #NOT SHOW AN ERROR "_Employee02" className '''Access Indirectly'''
a._Employee02__name="abcd"
print(a._Employee02__name,a._Employee02__work) #NOT SHOW AN ERROR "_Employee02" className '''Access Indirectly'''

print(a.__dir__())
print(type(a))
print(type(Employee02))
print(type(a._Employee02__name))

#PROTECTED ACCESS MODIFIER

class person:
    def __init__(self):
        self._name="SONU"
    def _func(self): #PROTECTED METHOD using "_"
        return("_func")

class student(person): #INHERITANCE CLASS
    pass

obj1=person()
obj2=student()

print(obj1._name)
print(obj1._func())
print(obj2._func())
print(obj2._name)
