#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def nextPrime(num):
    def prime(num):

        if num <= 1:
            return False
    
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    
    next_num = num + 1
    while not prime(next_num):

        next_num += 1
        
    return next_num

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        ans = nextPrime(n)
        print(ans)
