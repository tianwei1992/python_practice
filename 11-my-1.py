#11=my-1.py
##open a file and write something
f=open(r'F:\file1.txt','w+')
f.write('first\n')
f.write('second\n')
f.write('third\n')
f.close()
f=open(r'F:\file1.txt','r')
print(f.read(1))
print(f.read(2))
print()
print(f.read())
print()



#readline
#redlines
f=open(r'F:\file1.txt','r')
print(f.readline())
print(f.readline(10))
print(f.readlines())


#random access
f=open(r'F:\file1.txt','wb')
f.seek(2)
print(f.tell())
f.write('01'.encode())
f.seek(1,1)
print(f.tell())
f.write('001'.encode())
print(f.tell())
f.seek(-2,1)
print(f.tell())
f.seek(1,2)
print(f.tell())
f.write('0001'.encode())
f.close()
print()


f=open(r'F:\file1.txt','r')
print(f.read(4))
print(f.tell())
print()
