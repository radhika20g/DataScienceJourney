num = int(input("Enter a number: "))
temp = str(num)
power = len(temp)
#print(power)
sum = 0 
n = num
print(sum, n)
while n!=0:
    rem = n%10
    sum += rem**power
    n = n // 10

if sum == num:
    print(f'{num} is an armstrong number. Sum = {sum}')
else:
    print(f'{num} is not an armstrong number. Sum = {sum}')