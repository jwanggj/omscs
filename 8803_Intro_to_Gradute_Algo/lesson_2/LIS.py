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
express L[i] in terms of L[1], ... L[i]


longest subsequence with min ending char
"""

"""
DP Algorithm

L(i)=1+MAX(j){L(j):aj<ai & j<i}

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

def LIS(series):
    lis4everyChar = [1]
    for i in range(1, len(series)):
        lisEndCharSmlerThanCurrent = []
        for x in range(0, i):
            if series[x] < series[i]:
                lisEndCharSmlerThanCurrent.append(lis4everyChar[x]+1)
        if not lisEndCharSmlerThanCurrent:
            lis4everyChar.append(1)
            continue
        lis4everyChar.append(max(lisEndCharSmlerThanCurrent))
    return max(lis4everyChar)

if __name__ == '__main__':
    print(LIS([5,7,4,-3,9,1,10,4,5,8,9,3]))
    
