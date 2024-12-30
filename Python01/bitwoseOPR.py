#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def utility():
    #The following 3 lines take input. Don't change them!
    a=int(input())
    b=int(input())
    c=int(input())
    
    d = a ^ a
    e = c ^ b
    f = a & b
    g = c | (a ^ a)
    e = ~ e

    #The line below prints the output. Don't change it!
    print(d,e,f,g)

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