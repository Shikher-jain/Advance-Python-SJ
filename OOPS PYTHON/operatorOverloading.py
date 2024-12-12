class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self,x):
        # return f"{self.i+x.i}i + {self.j+x.j}j + {self.k+x.k}k"  #<class 'str'>
        return Vector(self.i+x.i, self.j+x.j , self.k+x.k)    #<class '__main__.Vector'>
        
    def __mul__(self,x):
        # return f"{self.i+x.i}i + {self.j+x.j}j + {self.k+x.k}k"  #<class 'str'>
        return Vector(self.i*x.i, self.j*x.j , self.k*x.k)    #<class '__main__.Vector'>

v1=Vector(3,5,6)
print("V1:\n",v1)
v2=Vector(1,-1,-2)
print("V2:\n",v2)

print("Add:\n",v1+v2)
print("Mul:\n",v1*v2)
print(type(v1+v2))