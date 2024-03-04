#Problem Statement - Set and Tuples - Two Sum Problem that returns a tuple of elements equal to given sum.
def two_sum_tuples(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        check = target - num
        if check in dic:
            return(check, num)
        dic[num] = i
    return None

nums = [2, 7, 11, 15]
target = 9
result = two_sum_tuples(nums, target)
print("Tuple of Elements:", result)
