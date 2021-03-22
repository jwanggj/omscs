"""
Dynamic Porgramming Intro
"""

"""
Method 1:Recursive Algorithm
Fib1(n):
    F[0] = 0  # O(1)
    F[1] = 1  # O(1)
    return F[n-1] - F[n-2] #  T(n-1) + T(n-2)

Let T(n)=# steps for Fib1(n)

T(n) <= O(1) + T(n-1) + T(n-2)
T(n) >= Fn = phi ^ n /sqrt(5)
where phi = (1+sqrt(5)) / 2

INEFFICIENT!!!

Method 2: Dynamic Programming
Fib2(n):
    F[0] = 0  # O(1)
    F[1] = 1  # O(1)
    for i=2->n:  # O(n)
        F[i] = F[i-1]+F[i-2]  # O(1)
    return F[n]  # O(n) total time


Dynamic Programming
- No recursion in algorithm
- Memoization

"""

"""
Dynamic Porgmming
- No recursion in algorithm
"""


def fibonacci_num(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f = 1
    f_1 = 0
    for i in range(2, n + 1):
        temp = f
        f += f_1
        f_1 = temp
    return f

if __name__ == '__main__':
    for i in range(10):
        print(fibonacci_num(i))
