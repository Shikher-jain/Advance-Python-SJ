s1={'a','b','c','d','e'}
s2={'f','g','h','i','j'}
s3={'k','l','m','n','o'}
s4={'p','q','r','s','t'}
s5={'u','v','w','x','y'}
s6={'z','0','1','2','3'}
s7={'4','5','6','7','8'}
s8={'9'}

print(type(s1))
for x in s1:
    print(x,end=" , ")
print("\n")

print('a' in s1)
print('a' in s2)
print('a' not in s1)
print('a' not in s2)

print(s8)
s8.add('-')
print("add",s8)
s8.update('_','+','=')
print("update",s8)

for x in s1:
    s8.add(x)
print("iteral",s8)

for i in s1:
    S=s8
    print(f"remove {i} from" ,S ,"--> ", end=" ")
    s8.remove(i)
    print(s8)

try:
    print(s7)
    s7.remove('j')
    print("remove",s7)
except:
    print(s7)
    s7.discard('a')
    print("discard",s7)

print(s7)
pop_item=s7.pop()
print("pop item :",pop_item)
print("pop",s7)
s7.add(pop_item)
print(s7)

try:
    print(s7)
    s7.clear()
    print("clear",s7)
except :
    print(s7)
    del s7
    print("del")

s7.update('4','5','6','7','8')
print("After Adds ('4','5','6','7','8') --> ",s7)

s9=s1.union(s2)
print("union",s9)
s10=s1|s2
print("|",s10)

s11=s4.intersection({'p','q','r'})
print("intersection {'p','q','r'} -->",s11)
s12=s4&s3
print("&",s12)

s13=s5.difference('x','y',s6)
print(f"{s5} difference {'x','y'} --> ",s13)
s14=s5-{'w','v'}
print(f"{s5} - {'w','v'} -->" ,s14)

s15=s6.symmetric_difference(s7)
print(f"symmetric_difference of {s6} and {s7} --> ",s15)
s15=s6 ^ s7
print(f"{s6} ^ {s7} --> ",s15)

s4.intersection_update(s3)
print("intersection_update",s4)

s4.intersection_update({'p','q','r'})
print("intersection_update",s4)

print(s5,"difference_update {'w','u'} ")
s5.difference_update('w','u')
print("difference_update",s5)

print(f"symmetric_difference_update of {s6} and {s7} ",end=" --> ")
s6.symmetric_difference_update(s7)
print(s6)

s16=s15.copy()
print(f"s15:{s15}\ns16:{s16}")


s0=set()
for i in range(1,input("Enter No.")+1):
    ip=int(input(f"Enter {i} element on set"))
    s0.add(ip)
    print(s0)
