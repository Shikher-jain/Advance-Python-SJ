def alphabets(c1,c2):
    for i in range(ord(c1),ord(c2)+1):
        print(chr(i),end=" ")
if __name__ == '__main__':
    c1 = input()
    c2 = input()      
    alphabets(c1,c2)
    print() 