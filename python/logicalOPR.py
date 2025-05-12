#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def utility():
    #The two lines below take input. Don't change them!
    a=int(input())
    b=int(input())
    
    #Do a and b below
    p = a and b
    #Do a and b below
    q = a or b
    #Do not a below
    r = not a

    #The code below prints the output. Don't change it!
    print(p,q,r)

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