from typing import Any


class Employee:
    def __init__(self, name):
        self.name=name

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return(i)

    def __str__(self):
        return (f"Name is {self.name} in str")
    
    def __repr__(self):    #In Case Of __str__ is not available
        return (f"Name is {self.name} in repr")

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("call")

print(__name__)
if (__name__=="__main__"):
    e1=Employee("Shikher")
    print(e1)
    print(e1.name)
    print(len(e1))
    e1()