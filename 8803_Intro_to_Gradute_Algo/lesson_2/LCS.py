"""
Goal: find the length of longest string which is a subsequence of both X & Y

Example X=BCDBCDA
y = ABECBAS

lenght of LCS = 4

Step 1: Desgin subproblem in words
    try same problem on prefix of input

    for i where 0<=i<=n,
    Let L(i)=length of LCS in X1...Xi, Y1...Yi

Step 2: Define recurrence



"""

"""
if xi=yi, then L(i)=1+L(i-1)

if xi!=yi, then LCS does not include Xi or Yi or (Xi & Yi)

    Need LCS(X1..Xi, Y1...Yi-1) !!!

"""

"""
Two indices i & j 2-D table

subproblem definiation:
for i & j where 0<=i<=n & 0<=j<=n
    Let L(i, j) length of LCS in X1...Xi, Y1...Yj

if Xi!=Yj: either Xi &/or Yj are not in optimal solution
    if drop Xi then L(i,j)=L(i-1,j)
    if drop Yj then L(i,j)=(i,j-1)

    L(i,j)=max{L(i-1,j), L(i,j-1)}

if Xi=Yj: either drop Xi, drop Yj or optimal solution ends at Xi = Yi

    L(i,j)=max{L(i-1,j), L(i,j-1), 1+L(i-1,j-1)}


Recurrence Summary
Let L(i,j)=length of LCS in X1..Xi, Y1...Yj

for i>=1, j>=1:
    L(i,j)= max{L(i-1, j), L(i, j-1)} if Xi!=Yj
            1+L(i-1,j-1) if Xi=Yj

"""

"""
DP Algorithm

LCS(X, Y):
    for i=0->n, L(i,0)=0
    for j=0->n, L(0,j)=0
    for i=1->n
        for j=1->n
            if Xi=Yj then L(i,j)=1+L(i-1,j-1)
                     else L(i,j)=max{L(i-1,j), L(i,j-1)}
    return L(n,n)

Running time O(n^2)

"""
def LCS(X, Y):
    L = [[0] * (1 + len(Y))]
    for i in range(len(X)):
        new_row = [0]
        for j in range(len(Y)):
            if X[i] == Y[j]:
                new_row.append(1 + L[-1][j])
            else:
                new_row.append(max(new_row[-1], L[-1][j+1]))
        L.append(new_row)
    return L[-1][-1]

if __name__ == "__main__":
    X = list("BCDBCDA") 
    Y = list("ABECBAS")
    print(LCS(X, Y)) 