# def avg(a,b):
#     print("The average is:",(a+b)/2)
# avg(5,9)

# def avg01(*num):
#     print(type(num),type(avg01))
#     sum=0
#     for i in num: 
#         sum=sum+i
#     print("The average is:",sum/len(num))
# avg01(1,2,3,4,5,6,7,8,9,10)

# def avg02(**names):
#     print(type(names),"\n",type(avg02))
#     print("yoo", names["abcd"] , names["efgh"] , names["ijkl"])
# avg02(abcd="mnop",efgh="qrst" ,ijkl="uvwx")

# def avg03(a,b):
#     return (a+b)/2
# avg04=avg03(5,9)
# print(avg04)

# list=[i*i for i in range(10)]
# print(list)

# list01=[i*i for i in range(10) if i%2==0]
# print(list01)

# list02=[i*i for i in range(10) if i%2!=0]
# print(list02)

# l =[3,7,1,8,4,2,9,6,5,0]
# print(l)
# l.sort(reverse=True)
# print(l)
# l.sort()
# print(l)
# l.append(11)
# print(l)
# l.remove(4)
# print(l)
# l.pop()
# print(l)
# l.reverse()
# print(l)
# l.reverse()
# print(l.index(2),"index")
# print(l)
# print(l.count(2),"count")
# m=l
# m[0]=4
# print(l)
# print(m)
# m2=l.copy()
# print("use copy function")
# print(l)
# print(m)
# l.insert(1,9)
# print(l)
# l2=[1,2,3,4]
# m3=[9,8,9,7,6]
# l.extend(m)
# print(l)
# l.sort()
# print(l)
# print(l2+m3)
# print("set\n",set(l))
a=0
while a==1:
    x=int(input("Enter the value of x : "))
    match x:
        case 1:
            print("x is 1")
        case 2:
            print("x is 2")
        case 3:
            print("x is 3")
        case 4:
            print("x is 4")
        case 5:
            print("x is 5")
        case 6:
            print("x is 6")
        case 7:
            print("x is 7")
        case _ if x!=8:
            print("x =",x)
        case _ :
            print("x =",x)

