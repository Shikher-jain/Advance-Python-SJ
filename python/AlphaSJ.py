#   E H I K R S


rows = 5

def S(rows):
    for i in range(rows):
        if i==0 or i== rows-1 or i==rows//2:
            print("* "*rows)
        elif i < rows//2:
            print("* ")
        else:
            print("  "*(rows-1),"*")

def H(rows):
    for i in range(rows):
        if i == rows//2:
            print("* "*(rows))
        else:
            print("* "," "*(rows-1),"*")

def I(rows):
    for i in range(rows):
        if i==0 or i==rows-1:
            print("* "*(rows))
        else:
            print(" "*(rows//2)," *")

def K(rows):
    for i in range(rows):
        ...
        if i == rows//2 :print("*  *")
        elif i < rows//2:print("*"," "*(rows-i-2),"*")
        else:print("*"," "*(i-rows//2),"*")

def E(rows):
    for i in range(rows):
        if i==0 or i==rows-1:
            print("* "*(rows))
        elif i==rows//2:print("* "*(rows-i))
        else:print("*")

def R(rows):
    for i in range(rows):
        if i==0 or i==rows//2:
            print("* "*(rows))
        elif i==1:print("* "," "*(rows-1),"*")
        elif i==rows//2:print("* "*(rows-i))
        else:print("* "," "*(i-rows//2)," *")
        


if __name__ == "__main__":
    ...
    S(rows)
    print()
    H(rows)    
    print()
    I(rows)
    print()
    K(rows)
    print()
    H(rows)
    print()
    E(rows)    
    print()
    R(rows)
    print()