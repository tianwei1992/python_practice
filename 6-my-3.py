#6-my-3.py
#a copy of list's modify
lst1=[1,2,3]
lst2=lst1
print('lst1=',lst1)
print('lst2=',lst2)
print()
lst2[0]=4
print('lst1=',lst1)
print('lst2=',lst2)
print()

lst3=lst1[:]
lst3[1]=5
print('lst1=',lst1)
print('lst3=',lst3)
print()
