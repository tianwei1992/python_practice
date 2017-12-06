#6-my-2.py
#fibs()
#func.__doc__



#not using nest


def fibs1(num):
        'not using nest'
        result=[1,2]
        for i in range((num-2)):
                #因为前两个数已知，所以只需计算后面的num-2个数
                result.append(result[-1]+result[-2])
        return result
print(fibs1(8))
print(fibs1.__doc__)
print(hasattr(fibs1,'__doc__'))

#using nest
import math
def fibs2(num):
        'using nest'
        if math.floor(num)!=float(num):
                raise Exception('must input a int')
        if num==1:
                return ([1])
        elif num==2:
                return ([1,2])
        else:
                new=fibs2(num-1)[-1]+fibs2(num-1)[-2]
                lst=fibs2(num-1)
                lst.append(new)
        return lst
print(fibs2(8.0))
print(fibs2.__doc__)

