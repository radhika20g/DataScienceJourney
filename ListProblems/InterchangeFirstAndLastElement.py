'''
Problem: Python program to interchange first and last elements in a list
Given a list, write a program to swap first and last element of the list.
Examples: 
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]
Input : [1, 2, 3]
Output : [3, 2, 1]
'''

lst = []
while True:
    num = input("Enter the number you want to add in list( to stop enter 'x'): ")
    if num!='x':
        lst.append(int(num))
    else:
        break

print("Original list:", lst)
temp = lst[0]
lst[0] = lst[len(lst)-1]
lst[len(lst)-1] = temp
print("Interchanged List:", lst)
