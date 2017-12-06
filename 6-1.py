#6-1.py
def search(sequence,number,lower=0,upper=None):
	if upper==None:
		upper=len(sequence)-1
	if lower==upper:
		assert number==sequence[upper]
		return upper
	else:
		middle=(upper+lower)//2
		if number>sequence[middle]:
			return search(sequence,number,middle+1,upper)
		#此处省略了单独判断number==sequence[middle]，把它全部归纳到else里面，这是必要的，因为：
		#二分法本来就是为提高效率而生，每次＞判断可以将搜索范围缩小一半。
		#所以如果单独判断number==sequence[middle]，是在拉低效率
		##因此在有重复元素时，处理会有差异
		#对于print(search([0,0,1],0))，结果是0，而不是1。
		#print(search([1,2,2],2))报1
		else:
			return search(sequence,number,lower,middle)
		#所以这里用的middle而不是middle-1
		#还顺便巧妙避开了print(search([0,1],0))出错的问题
print(search([0,1],0))
print(search([0,1],1))
print(search([0],0))
print(search([0,0,0],0))
print(search([0,1,0],1))
print(search([0,0,1],0))
print(search([1,2,2],2))

