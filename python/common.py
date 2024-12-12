def max(a,b):
    if a<b:
        return a
    elif a==b:
        return "both a and b are equal"
    else:
        return b
    
def min(a,b):
    if a>b:
        return a
    elif a==b:
        return "both a and b are equal"
    else:
        return b
    
def table(n):
    for i in range(n,n*10+1,n):
        print(i)

