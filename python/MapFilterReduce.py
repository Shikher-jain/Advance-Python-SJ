l=[1,2,4,6,4,3]
# def cube(x):
#     return x**3

# print(cube(8))

# # newl=[]
# # for i in l:
# #     print(cube(i))
# #     newl.append(cube(i))
# # print(newl)

# # newl2=map(cube,l)
# # print(newl2)
# newl2=list(map(cube,l))  #map(function, iterable or list,tuple)
# print(newl2)

# def filterFunction(a):
#     return a>2

# newl3=filter(filterFunction,l)  #filter(predicate, iterable - list, tuplbe)
# newl4=list(filter(filterFunction,l))
# print(newl3)
# print(newl4)

from functools import reduce
l1=[1,2,3,4,5]
sum =reduce(lambda x,y:x+y,l1)
print(sum)
