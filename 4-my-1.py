#4-my-1.py
#3ways to create a dictory

#1 way
dic1={'A':1,'B':2,'C':3}

dic2=dict([('A',1),('B',2),('C',3)])

dic3=dict(A=1,B=2,C=2)

print('dic1:',dic1,'\n')
print('dic2:',dic2,'\n')
print('dic3:',dic3,'\n')


#basic operation
print('len[dic1]:',len(dic1),'\n')
print("'A' in dic1",'A' in dic1,'\n')
print("dic1['A'] :",dic1['A'] ,'\n')
dic1['A']=4
print("dic1['A']=4,AND THEN diC1:",dic1,'\n')
del dic1['A']
print("dic1['A'] di1:",dic1,'\n')


dic2=dict([('A',1),('B',2),('C',3)])
print(dic2.keys())
name=input('input name within ABC:')
print("%s 's phone number is %d"%(name,dic2[name]))
print("%s s phone number is "%name,end='')
#print("%(value)s"%{"key":name,"value":dic2[name]})
print("%(value)s"%{"value":dic2[name]})
