import threading
import time

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

# func(4)
# func(3)
# func(1)
# time2=time.perf_counter()
# print(time2-time1)

t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[1])

time3=time.perf_counter()
t1.start()
t2.start()
t3.start()

# t1.join()
# t2.join()
# t3.join()

time4=time.perf_counter()
print(time4-time3)