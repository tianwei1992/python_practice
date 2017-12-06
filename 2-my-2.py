#2-my-2.py
#something about list
# join and list,how to use ?


'''str=''.join('a','b','c')
TypeError: join() takes exactly one argument (3 given)
'''
str=''.join(['a','b','c','d'])
print ('str:',str)

lst=list(str)
print('lst:',lst)

#Partition assignment 
lst2=[1,2,3,4]
lst3=[1,2,3,4]
lst2[0:2]=lst[1:3]
lst3[:]=lst[:-2]
print('lst2:',lst2)
print('lst3:',lst3)
#Partition assignment to insert
lst_insert=lst[:]
lst_insert[3:3]=[3]
print('Partition assignment to insert:lst_insert[3:3]=[3]')
print(lst_insert)
lst_insert[3:4]=[]
print('lst_insert:lst_insert[3:4]=[]')
print(lst_insert)


#del 
del lst[1]
print('del:',lst)

#listfunctions

#append
lst4=['a','p','e','n']
lst4.append('d')
print('apend:lst4=','\n',lst4,'\n')

#count
print('count:"e" in lst4 :',lst4.count('e'),'\n')


#extend

print('extend:',lst4.extend(['extend']))
print('lst4:',lst4,'\n')

#index
print('index:',lst4.index('p'),'\n')

#insert
print('insert2,"p":',lst4.insert(2,'p'))
print('lst4:',lst4,'\n')

#pop
lst4.pop()
print('after pop,lst4:',lst4,'\n')

#remove
print('after remove "d",lst4:',lst4.remove('d'))
print('lst4:',lst4,'\n')


#reverse
print('after reverse lst4:',lst4.reverse())
print('lst4:',lst4,'\n')
#sort
print('after sort lst4:',lst4.sort())
print('lst4:',lst4)

