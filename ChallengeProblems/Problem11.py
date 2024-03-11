'''
Problem Statement - Functions :
Calculating the nth term of the Ackermann function.
The Ackermann function is a recursive mathematical function that is exceptionally fast-growing. It is often used to demonstrate the difference in growth rates between simple recursive algorithms and more efficient ones.

If m = 0, the result is n + 1.

If m > 0 and n = 0, the result is ackermann(m-1, 1).

If m > 0 and n > 0, the result is ackermann(m-1, ackermann(m, n-1)).
'''

def ackermann(m,n):
    if m == 0:
        return n+1
    if m>0 and n==0:
        return ackermann(m-1, 1)
    if m>0 and n>0:
        return ackermann(m-1, ackermann(m, n-1))
    
result = ackermann(3,4)
print(result)