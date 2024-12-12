import time
# print(dir(time))
forList=[]
whileList=[]
init=time.time()
print(time.time())
for i in range(10):
    forT=(time.time()-init)
    print(i ,"->",time.time())
    print(i ,"->",forT,"in ms")
    forList.append(forT)
j=0
while j<=10:
    whileT=(time.time()-init)
    print(j ,"->",time.time())
    print(j ,"->",time.time()-init,"in ms")
    whileList.append(whileT)
    j+=1
print(forList)
print(whileList)

sec=int(input("Enter The Second: "))
print(12345)
time.sleep(sec)
print(f"Print After {sec} Of Sleep")

t= time.localtime()
format=time.strftime("%Y-%m-%d-->%H:%M:%S")
print(format)
