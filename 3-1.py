#3-1.py
#string format%vlue
#

#v1.0

width=int(input('input width:'))
price_width=10
item_width=width-price_width


print('='*width)
print('%-*s%*s'%(item_width,'Item',price_width,'Price'))
print('-'*width)
print('%-*s%*.2f'%(item_width,'Apples',price_width,0.4))
print('%-*s%*.2f'%(item_width,'Pears',price_width,0.5))
print('%-*s%*.2f'%(item_width,'Bananas',price_width,1.92))
print('%-*s%*.2f'%(item_width,'Dried AP=pricots',price_width,8))
print('%-*s%*.2f'%(item_width,'Prunes',price_width,12))



#v2.0 :code optimization
header_format='%-*s%*s'
format='%-*s%*.2f'
print('\n\n\n')
print('='*width)
print(header_format%(item_width,'Item',price_width,'Price'))
print('-'*width)
print(format%(item_width,'Apples',price_width,0.4))
print(format%(item_width,'Pears',price_width,0.5))
print(format%(item_width,'Bananas',price_width,1.92))
print(format%(item_width,'Dried AP=pricots',price_width,8))
print(format%(item_width,'Prunes',price_width,12))

