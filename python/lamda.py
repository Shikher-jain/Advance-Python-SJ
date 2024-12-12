#function 
# def example(x):
    # return x*2
# print(example(10))

# lamda function :

X2=lambda x:x**2
X3=lambda x:x**3
XYZ=lambda x,y,z:x*y*z
print(X2(int(input("Enter no. for square: "))))
print(X3(int(input("Enter no. for cube: "))))
print("x*y*z = ",XYZ(int(input("Enter no. for 'x': ")),int(input("Enter no. for 'y': ")),int(input("Enter no. for 'z': "))))