# 赋值运算符 
'''
= | c = a + b 将 a + b 的运算结果赋值为 c
+= | c += a 等效于 c = c + a
-= | c -= a 等效于 c = c - a
*= | c *= a 等效于 c = c * a
/= | c /= a 等效于 c = c / a
%= | c %= a 等效于 c = c % a
**= | c **= a 等效于 c = c ** a
//= | c //= a 等效于 c = c // a
'''
a=20
b=10
print('a=',a,'b=',b)
a+=b
print('a+=b:',a)
a*=b
print('a*=b:',a)
a//=b
print('a//=b:',a)
input()