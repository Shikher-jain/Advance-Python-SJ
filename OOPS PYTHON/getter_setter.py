class Myclass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"Value = {self._value}")
    @property
    def value(self):
        return self._value

    @property
    def mul10(self):
        return 10* self._value
    
    @value.setter
    def value(self,nvalue):
        self._value=nvalue

    @mul10.setter
    def mul10(self,nvalue10):
        self._value=nvalue10/10
    
obj = Myclass(7)
obj.show()
obj.value=5
obj.show()
obj.mul10=10
obj.show()
print(obj.value)
print(obj.mul10)
obj.show()