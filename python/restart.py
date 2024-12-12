a  =input("Enter \"any\" no.")
print (a*7,"\t")
# print("\t") 
b =input("Enter \"any\" no.")
print(b*5)
print("hi \n"*7) 
prt="""hi
hello'ji'
bye
"""
print(prt)

ex1="shikher jain"
for i in ex1:
    print(i)
print(ex1)
print("Slicing 0 to 8",ex1[0:8])
print("Slicing 8 to 13",ex1[8:13])
print("hello",99,00,sep="!",end="#001\n")
'''
sep=" " is for seperating space b/w string & outputs
end=" " is for next string first elements i.e
'''
print("\n",2)
c="python"
print(c)
d=777
e=987.4
f=complex(3,9)
g=True
h=False
print(a+b)  #to join two same type of data type i.e. concatenate
print(d+e)#to join two same type of data type i.e. concatenate
print("The type of a is",a,type(a))
print("The type of c is",c,type(c))
print("The type of d is",d,type(d))
print("The type of e is",e,type(e))
print("The type of f is",f,type(f))
print("The type of g is",g,type(g))
print("The type of h is",h,type(h))
#========== operators==========#
print(19+19,"addition")
print(29-13,"substraction")
print(12*67,"multiplication")
print(76/3,"division")
print(12/6,"division")
print(122//4,"non-decimal division")
print(15%6,"modulus")
print(3**5,"exponential")

list=[1,2,3,4,6,7,3,45,2,6,8,4,4,8,6,0,0,9,8,7799,6,9,8,7,8,7]
list.sort()
print("the sorted list is\n", list)
del(list[3])
print("after use del function","\n",list)
b="shikher_jain"
print(b[0:6])
print(b[0:-4])
print(b[-4:-1])
print(b[3:8])#slicing
print("The lenght of string is",len(b),)
print("The elements ina list are",len(list),)
c="mango"
print(c[-3:-1])
print(b.upper()) 
print(c.capitalize())
d="!@#$shikher!$@!!##"
print(d.rstrip("! # @ $"))
e=input("Enter text using 'sonu':--> ")
print(e.replace("sonu","shikher"))
print(e.split(" "))
f="welcome ti vs code bhaii"
print(f.center(105))
print(len(f))
print(len(f.center(105)))
print("Repeation of sonu  ",e.count("sonu"))
print(e.endswith(""))
e1="welcome to python programming"
print(e1.split(" "))
print(e1.endswith("o",6,8))
print(e1.endswith("o",6,7))
print(e1.endswith(" ",6,8))
f="kya haal chal hai mota bhai"
print(f.find("chal")+1)
print(f.find("hi")+1)
print(f.index("chal")+1)
# print(f.index("hi")+1)#error
print("isalnum",f.isalnum())
print("isalpha",f.isalpha())
print("isascii",f.isascii())
print("islower",f.islower())
print("isupper",f.isupper())
print("isprintable",f.isprintable())#\n \t not used
print("isspace",f.isspace())
print("istitle",f.istitle())# check the first letter is capitalized or not 
print("startswith",f.startswith("kya"))
print("endswith",f.endswith("bhai"))
print("swapcase",f.swapcase() )
print("title",f.title())#change the first letter is capitalized or not 
print("spliting",f.split(' '))

g=int(input("Enter your age  "))
if(g>18):
    print("You can vote")
elif(g==18):
    print("You can also vote now")
else:
    print("You can not vote now\nPlease wait",18-g,"years for vote")
    
    
print(g<18)
print(g>18)
print(g<=18)
print(g>=18)
print(g!=18)
print(g==18)