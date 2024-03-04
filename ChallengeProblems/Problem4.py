#Problem Statement - Multidimensional list - Finding maximum value in a 2 D list.
lst = [[1,5,9], [7,3,2], [4,2,5]]
maxm = 0
for i in lst:
    maxm = max(maxm, max(i))

print(maxm)