def Fx(n):
    return lambda a:a*n

Double =Fx(2)
Triple =Fx(3)

print(Double(int(input("Enter no. for Double: "))))
print(Triple(int(input("Enter no. for Triple: "))))
