'''
Problem: Check if an element exists in a list in Python
Example:
Input: test_list = [1, 6, 3, 5, 3, 4]
            3  # Check if 3 exist or not.
Output: True
Explanation: The output is True because the element we are looking is exist in the list.
'''

lst = [1, 6, 3, 5, 3, 4]

#1. Using “in” Statement
# checking if 3 exists in list [1, 6, 3, 5, 3, 4]
print(3 in lst)
print('-'*50)

#2. Using loop
#Checking if 4 exists in list [1, 6, 3, 5, 3, 4]
flag = 0
for i in lst:
    if i == 4:
        print("Element exists")
        flag = 1
        break
   
if flag == 0:
    print("Element does not exist")

print('-'*50)


#3. using the count() function
#checking if 6 exists in the list [1, 6, 3, 5, 3, 4]
exist_count = lst.count(6)

if exist_count > 0:
    print("Yes, 6 exists in list")
else:
    print("No, 6 does not exists in list")
print('-'*50)