#Program to Swap Two Elements in a List
'''Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 

Examples:  

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]'''

user_inp = input("Enter the list elements: ")
lst = [int(item) for item in user_inp.split(' ')]
pos1 = int(input("Enter first position: "))
pos1 -= 1
pos2 = int(input("Enter second position: "))
pos2 -= 1
print("Original List:", lst)
lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
print("New list:", lst)