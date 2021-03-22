"""
Longest Increasing Subsequencces (LIS)
Input: n numbers a1, a2, ... an
Goal: find length of LIS in a1, ...an

example:
5,7,4,-3,9,1,10,4,5,8,9,3

substring=set of consecutive elements
subsequence=subset of elements in order (can skip)

LIS=-3,1,4,5,8,9
output = 6
"""

"""
DP solution

1st step: define subproblem in words
Let L[i] length of LIS on a1, a2, ... an, which includes ai

2nd step: state recursive relation
express L[i] in terms of L[1], ... L[i-1]

A = 5,7,4,-3,9,1,10,4,5,8,9,3
L = 1,2,1, 1,3,2, 4,3,4,5,6,
longest subsequence with the min ending char
"""

"""
DP Algorithm
L(i)=1+MAX{L(j):aj<ai & j<i}


LIS(a1,...an):
    for i=1->n:
        L(i)=1
        for j=1->i-1:
            if aj < ai & L(i) < 1+L(j)
                then L(i)=1+L(j)
    max = 1
    for i=2->n:
        if L[i]>L(max) then max=i
    return L(max)

"""

"""
Runing time
O(n^2)
"""

def LIS(series):
    L = [1] * len(series)
    for i in range(len(series)):
        for j in range(0, i):
            if series[j] < series[i] and L[i] < L[j] + 1:
                L[i] = 1 + L[j]
    MAX = 0
    for i in range(len(L)):
        if L[i] > L[MAX]:
            MAX = i
    return L[MAX]

if __name__ == '__main__':
    print(LIS([5,7,4,-3,9,1,10,4,5,8,9,3]))
    
