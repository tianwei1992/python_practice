#11-my-2.py
#open(f,'wb')
#what's different in binary

f=open('file3.txt','w')
f.writelines(['first lines:tianwei\n','second lines:lihong\n','third lines:tianguangzhi\n'])
f.writelines(['fourth lines:haha\n'])
f.close()

f=open('file3.txt','r')
print(f.readlines())
f.seek(0)
for i in range(3):
	print(f.readline())


