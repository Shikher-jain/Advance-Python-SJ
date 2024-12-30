#{ 
 # Driver Code Starts
#Initial Template for Python 3



# } Driver Code Ends
#User function Template for python3

def utility():
    #The following lines take the input. Don't change them!
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    
    '''
     a + b
    ______  +  d
       c
    '''
    #Complete the code below that stores the output of the expression         
    res = (a+b)//c + d
    #Complete the code above that stores the output of the expression
    
    #This prints the output. Don't change it!
    print(res)

#{ 
 # Driver Code Starts.

def main():
    t=int(input())
    while(t>0):
        utility()
        t-=1

if __name__ == "__main__": 
    main()
# } Driver Code Endshttps://media.geeksforgeeks.org/wp-content/uploads/20200819111131/IMG0317-300x154.PNG