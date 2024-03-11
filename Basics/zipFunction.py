lst1 = ['A', 'B', 'C']
lst2 = [1, 2, 3]
print(list(zip(lst1, lst2)))
print('-'*50)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print([list(row) for row in zip(matrix)])
print([list(row) for row in zip(*matrix)])
print([list(row) for row in zip(*[list(row) for row in zip(matrix)])])
print('-'*50)

lst1 = [1,2,3]
lst2 = [4,5,6]
print(list(zip(lst1, lst2)))
print(list(i*j for i,j in zip(lst1, lst2)))
print(sum(list(i*j for i,j in zip(lst1, lst2))))
