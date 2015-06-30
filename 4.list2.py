list1=[1,2,3]
list2=[4,5,6]
print('list1:',list1)
print('list2:',list2)
print('list1长度为:',len(list1))
listSum=list1+list2
print('组合:',listSum) #组合
print('listSum长度为:',len(listSum))
del(listSum[3]) #删除
print('删除了listSum[3]')
print(listSum)
print('重复list1:',list1*3) #重复
print(3 in list2) #元素是否存在于列表中
for x in listSum:print(x) #迭代
input()