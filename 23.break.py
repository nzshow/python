# break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。break语句用在while和for循环中。

for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print('Current Letter :', letter)
 
var = 10                    # Second Example
while var > 0:              
   print('Current variable value :', var)
   var = var -1
   if var == 5:
      break
 
print("Good bye!")
input()