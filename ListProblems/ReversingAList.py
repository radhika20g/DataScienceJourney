'''
Problem: Reversing a List in Python
Example: 
Input: list = [4, 5, 6, 7, 8, 9]
Output: [9, 8, 7, 6, 5, 4] 
Explanation: The list we are having in the output is reversed to the list we have in the input.
'''

# 1. Reversing a list by slicing
lst = [1,2,3,4,5]
print(lst[::-1])

# 2. Reversing by swapping first and last element
def list_reverse(arr,size):
	if(size==1):
		return arr
	elif(size==2):
		arr[0],arr[1],=arr[1],arr[0]
		return arr
	else:
		i=0
		while(i<size//2):
			arr[i],arr[size-i-1]=arr[size-i-1],arr[i]
			i+=1
		return arr

arr=[1,2,3,4,5,6]
size=6
print('Original list: ',arr)
print("Reversed list: ",list_reverse(arr,size))

#3. 