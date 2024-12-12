# :=

# a=True
# print(a)
# print(a:=False)
# print(a)

# foods =list()
# while True:
#     food=input("Enter food name: ")
#     if food =="quit" or "exit":
#         break
#     elif food=="show":
#         print(foods)
    # foods.append(food)

#   walrus operator

# foods=list()
foods=[]
while(food:=input("Enter Food: "))!="quit":
    foods.append(food)
print(foods)