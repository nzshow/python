'''
for iterating_var in sequence:
      statements(s)
else:
      statements(s1) 
'''
num=10
for i in range(2,num):	#to iterate on the factors of the number
   if num%i == 0:		#to determine the first factor
       j=num/i			#to calculate the second factor
       print('%d equals %d * %d' % (num,i,j))
   else:				# else part of the loop
       print(num, 'is a prime number')
input()