dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print('Alice:',dict['Alice'])
print('Beth:',dict['Beth'])
print('Cecil:',dict['Cecil'])
dict['School'] = "DPS School"; # 增加键为'School'的条目
print(dict)
dict['Name']="Jim";            # 修改键为'Name'的条目的值
print(dict)
del dict['Name'];              # 删除键是'Name'的条目
print(dict)
dict.clear();                  # 清空词典所有条目
print(dict)
del dict ; 
print(dict)
input()