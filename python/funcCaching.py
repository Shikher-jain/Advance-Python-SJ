import functools
import time

# @functools.lru_cache(maxsize=None)
# def fx(n):

#     if n < 2:
#         return n
#     return fx(n-1) + fx(n-2)

# print(fx(20))


@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*5

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(10))
print("done for 10")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(120))
print("done for 120")