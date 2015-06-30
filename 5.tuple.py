tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
tup4 = ();    # 创建空元组
tup5 = (50,); #元组中只包含一个元素时，需要在元素后面添加逗号。
print('tup1:',tup1)
print('tup2:',tup2)
print('tup3:',tup3)
print('tup4:',tup4)
print('tup5:',tup5)
print(tup1+tup2)
print(tup1[2])
input()



#Python的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。
#注意：元组与字符串类似，下标索引从0开始，可以进行截取，组合等。