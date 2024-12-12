# p="print hai bhai\n"
# text=" a c d e f g h i j k l m n o p q s t u v w x y z"
# new=["a\n","b\n","c\n","d\n","e\n","f\n","g\n","h\n","i\n","j\n","k\n","l\n","m\n","n\n","o\n","p\n","q\n","r\n","s\n","t\n","u\n","v\n","w\n","x\n","y\n","z\n"]
# f=open("text.txt","a")
# f.write(text)
# f.close
# print(f)
# f=open("text.txt","r")
# print(f.read)
# f.close
# print(f)
# f=open("text.txt","a")
# f.writelines(text)
# f.close
# print(f)
# f=open("text.txt","r")
# r=f.readlines()
# print(r)
# f.close
# print(f)


# with open("text.txt","w") as f:
#     f.writelines(new)
# with open("text.txt","r") as f:
#     print(f.read)
# with open("text.txt","a") as f:
#     pr=p.split(",")
#     print(p)
#     print(pr)
#     f.writelines(pr)
#     f.write(p)
script="Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente, ab alias cum, fuga optio odit perspiciatis quo ducimus corrupti ullam adipisci? Libero cupiditate illo odit officiis placeat error vel asperiores cumque nulla eligendi rem quasi cum, autem deserunt vero? Praesentium voluptatum soluta temporibus. Consequatur quasi repellendus ratione, voluptatum perspiciatis ad!"

with open ("text.txt","w")as f:
    f.write(script)
with open ("text.txt","r")as f:  
    print(type(f))
    print(f.tell())
    f.seek(10)
    print(f.tell())
    print(f.read(15))
    print(f.tell())
with open ("text.txt","a")as f:
    f.truncate(70)
    f.writelines("\nHello!! bro")
# EOF -> End Of File