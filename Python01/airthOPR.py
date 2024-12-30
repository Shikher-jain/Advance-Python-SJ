#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def utility():
    #The below code takes input of x and y. Don't change it!
    a=int(input())
    b=int(input())
    
    # Perform addition x+y below
    p = (a + b)
    # Perform subtraction x-y below
    q = (a - b)
    # Perform multiplication x*y below
    r = (a * b)
    # Perform float division x/y below
    s = (a / b)
    # Perform integer divison x//y below
    t = (a // b)
    # Perform modulo operation x%y below
    u = (a % b)
    # Perform power(x,y) x**y below
    v = (a ** b)
    
    #The below code prints the output. Don't change it!
    print(p,q,r,"{:.5f}".format(s),t,u,v)

#{ 
 # Driver Code Starts.



def main():
    t=int(input())
    while(t>0):
        utility()
        
        t-=1

if __name__ == "__main__": 
    main()
# } Driver Code Ends