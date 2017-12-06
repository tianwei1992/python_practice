#3-my-2.py
# string functions

import string
#find
namestr='tian weiwei'
print('The index of a in str is:',namestr.find('a'),'\n')
print('The index of space in str is:',namestr.find(' '),'\n')

#find in certain range
print('The index of "wei" in str range (0,5) is:',namestr.find('wei',0,5),'\n')
print('The index of "wei" in str range (6:) is:',namestr.find('wei',6,),'\n')

#join
#!the arguments of join must be string
#sep.join(seq)
str1='+'.join('123')
print("str5='+'.join('123'),then",'\n'+'str1:',str1)
 
str2=''.join('123')
print("str2=''.join('123'),then",'\n'+'str2:',str2)
print('\n')


#split
str3=str1.split('+')
str4='tian wei'.split()
print('str3:',str3)
print('str4:',str4)
print('\n')


#strip
#remove spaces or certain character besides
str5='   tian wei with space  '
str6=str5.strip()
print('str5:',str5)
print('str6:',str6)
print('\n')

str5='!!!!tian !!! wei !!!!'
str6=str5.strip('!')
print('str5:',str5)
print('str6:',str6)
print('\n')


#lower upper capwords
str7='tian wei'
str8=str7.upper()
str9=str8.lower()
import string
str10=str8.capitalize()
print('str7:',str7)
print('str8:',str8)
print('str9:',str9)
print('str10:',str10)
print('\n')



#replace

str10='tian wei 24'
str11=str10.replace('24','age')
print('str10:',str10)
print('str11:',str11)
print('\n')

#translate
#for replace 2or more words at a time
#usage has chagend in 3
import string

table=''.maketrans('!*','na')
str10='ti*! wei 24'
str11=str10.translate(table)
print('str10:',str10)
print('str11:',str11)
print('\n')






