#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def utility():
    #The three lines below take the input. Don't change them!
    a=int(input())
    d=int(input())
    n=int(input())
    
    #Complete the code below
    ans =  a + (n-1)*d
    #Complete the code above
    
    #The line below prints the output. Don't change it!
    print(ans)

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        utility()
# } Driver Code Ends