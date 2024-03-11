lst = [1,2,3,4,5,6,7,8,8,9]
def is_even(n):
    return n%2 == 0

print(list(filter(is_even, lst)))
print('-'*50)

lst =[12,56,232,1,5,6,77]
lst1 = [1,2,3,4,5,6,7,8,9]

check_even = lambda x: x%2==0

print(list(filter(check_even, lst)))
print(list(filter(check_even, lst1)))
print('-'*50)
