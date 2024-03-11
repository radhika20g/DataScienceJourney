mul_num = lambda x,y: x*y
print(mul_num(5,2))
print('-'*50)

add_num = lambda x,y: x+y
print(add_num(45,9))
print('-'*50)   

check_even = lambda x: x%2 == 0
lst1 = [1,2,4,5,6,7,8,9]
print(list(i for i in lst1 if check_even(i)))
print('-'*50)   

from functools import reduce
num = [1,2,3,4,5]
product = lambda x,y: x*y
result = reduce(product, num)
print(result) 
