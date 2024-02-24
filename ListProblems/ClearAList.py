'''
Problem: Clear a list
Example: 
Input: [2, 3, 5, 6, 7]
Output: []
Explanation: Python list is cleared and it becomes empty so we have returned empty list.
'''

#1. using clear
lst = [1,2,3,4,5,6,7,8,9]
print("List before:", lst)
lst.clear()
print("List after:", lst)
print('-'*50)

#2. Reintialize the List
lst1 = [1,2,3,4,5]
print("List before:", lst1)
lst1 = []
print("List after:", lst1)
print('-'*50)

#3. Using “*= 0”
lst2 = [2,4,6,8,10]
print("List before:", lst2)
lst2 *= 0
print("List after:", lst2)
print('-'*50)
