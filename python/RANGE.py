import time
a=range(1,10001)
a="shikher jain"
print(a)
ans=""
for j in range(ord('a'), ord('z') + 1): 
    for i in a:
        
        ans+=i
        time.sleep(0.4)
        print(ans)

    