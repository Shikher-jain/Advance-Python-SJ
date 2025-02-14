f = open('Advance-Python-SJ\FILE HANDLING\myfile.txt','w')
print(f)
print(f.name)
f.write('Hello World')
f.close()

f = open('Advance-Python-SJ/FILE HANDLING/myfile.txt','r')
r=f.read()
print(r)
f.close()


fa = open('Advance-Python-SJ/FILE HANDLING/myfile.txt','a')
fr = open('Advance-Python-SJ/FILE HANDLING/myfile.txt','r')
r=fr.read()
print(r)
fa.write(r)
fr.close()
# fa.close()
print(fa.closed)

with open('Advance-Python-SJ/FILE HANDLING/myfile.txt','r') as f:
    print(f.read())

print(f.closed)