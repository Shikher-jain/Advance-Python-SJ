def mul():
    a,b=int(input("Enter first no. to mul:")),int(input("Enter second no. to mul:"))
    print("answer is ",a*b)
def sum():
    a,b=int(input("Enter first no. to sum:")),int(input("Enter second no. to sum:"))
    print("answer is ",a+b)
def sub():
    a,b=int(input("Enter first no. to sub:")),int(input("Enter second no. to sub:"))
    print("answer is ",a-b)
def div():
    a,b=int(input("Enter first no. to div:")),int(input("Enter second no. to div:"))
    print("answer is ",a/b)
    print("answer is ",a//b,"(floor)")
def exp():
    a,b=int(input("Enter first no. to exp:")),int(input("Enter second no. to exp:"))
    print("answer is ",a**b)
def mod():
    a,b=int(input("Enter first no. to mod:")),int(input("Enter second no. to mod:"))
    print("answer is ",a%b)
print(__name__)
if __name__=="__main__":
    mul()
    sum()
    sub()
    div()
    exp()
    mod()