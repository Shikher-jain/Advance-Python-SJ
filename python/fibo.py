
def fibonacci(n):

        n1,n2 = 1,1
        n3=n1+n2
        for i in range(n):
            n1,n2 = n2,n3
            n3=n1+n2
            # n3=n1+n2
            print(n1,n2,n3)
        return n2-n1


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        n=18
        ans = fibonacci(n)
        print(ans)
# 1 1 2 3 5 8 13