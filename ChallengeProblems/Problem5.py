#Problem Statement - Write a program to print Prime numbers in a given range.
n = int(input("Enter the number till which you want to print the prime numbers: "))
prime = []
flag = 0
for i in range(2, n):
    flag = 0
    for j in range(2, i):
        if i%j == 0:
            flag = 1
    if flag==0:
        prime.append(i)

print(prime)