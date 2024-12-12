# class person:
#     name="Shikher"
#     work="developer"


#     def info(self):
#         print(f"{self.name} is a {self.work}")
    
# a=person()
# print(a.name,a.work)
# a.info()

class Person:
    def __init__(self,name,work):
        self.name=name
        self.work=work
        print("This is Constructor !!")
        print(f"{self.name} is a {self.work}")
    def info(self):
        print(f"{self.name} is a {self.work}")
a=Person("SHIKHER","OWNER")
b=Person("shiker","owner")
a.info()
b.info()