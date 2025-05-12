import random
# a=random.randrange(1,100)
# count=0
# while(1):
#     b=int(input("Enter no.:"))
#     if b<=100:
#         if(a==b):
#             print("a is equal to b")
#             count+=1
#             print(f"You takes {count} moves")
#             break
#         elif a>b:
#             print(f"Try a no. which is greater than {b}")
#             count+=1
#         else:
#             print(f"Try a no. which is smallest than {b}")
#             count+=1
#     else:
#         print(("Enter the Value smallest than or equal t0 100"))

# A=[]
# a=[]
# for i in range(ord("A"),ord("Z")+1):
#     A.append(chr(i))
# for i in range(ord("a"),ord("z")+1):
#     a.append(chr(i))
# B=random.choice(A)
# b=random.choice(a)
# print(B)
# print(b)

# name=input("Enter name: ")
name="shikher"
# name=list(name)
n=len(name)
for i in range(n):
    print(random.choice(name),end="")