def gcd(a, b):
    for i in range(max(a,b),0,-1):
        if(a%i==0 and b %i==0):
            return i
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        A=int(input())
        B=int(input())
        
        ans = gcd(A,B)
        print(ans)
