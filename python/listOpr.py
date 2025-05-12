list1 = (0.5 * x for x in range(0, 4))  # Generator expression
for val in list1:
    print(val)
list1 = [0.5 * x for x in range(0, 4)]  # Using list comprehension
print(list1)
