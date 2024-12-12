x=[1,8,0,7,59,4,7.0]
print (dir(x))
print(x.__add__)

class Example:
    def __init__(self,name,age):
        self.name=name
        self.age=age

ex=Example("Shikher Jain",19)
print (ex.__dict__)

print(help(Example))