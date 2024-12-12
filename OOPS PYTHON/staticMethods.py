class Math:
    def __init__(self,num):
        self.num=num
    def addNum(self,n):
        self.num=self.num+n
    @staticmethod
    def add(a,b):
        return a+b
    
# result=Math.add(67,9)
# print(result)
a=Math(44) 
print(a.add(77,13))
print(a.num)
a.addNum(56)
print(a.num)
