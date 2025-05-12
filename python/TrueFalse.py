# True=False

# while(True):print(True);break


# var=10
# for i in range(10):
#     for j in range(2,10,1):
#         if var%2==0:
#             continue
#             var+=1
#             var+=1
#         else:
#             var+=1
# print(var)

# for i in range(int(2.0)):
#     print(i)

for num in range(10,14):
    for i in range(2,num):
        if num%i==1:
            print(num)
            break