# function
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return (n * fact(n-1))
 
print(__name__)
if __name__=="__main__":
    n=int(input("Enter a number: "))
    ans=fact(n)
    print(ans)
    print(__name__)