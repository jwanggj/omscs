"""
Example: 4 matrices A,B,C,D

Goal: compute A*B*C*D most efficiently

Say
    A is of size 50 * 20
    B is 20 * 1
    C is 1 * 10
    D is 10 * 100


standard way: ((A*B)*C)*D
                or (A*B)*(C*D)
                or (A*(B*C))*D
                or A*(B*(C*D))
            
            which is best


Cost for matrix Multiply
Take W of size a*b & Y of size b*c
Z = W * Y is of size a * c

abc multiplications
ac(b-1) additions

cost abc

for n metrices A1, A2, ..., An where Ai is mi-1 * mi

Input: m0, m1, ..., mn
Goal: what is the min cost for computing A1 * A2 * ... * An
"""

"""
DP Solution: attempt 1
Let C(i) = min cost for computing A1*A2*...*Ai

* substrings
For i&j where 1<=i<=j<=n
    let C(i,j) = min cost for computing Ai*Ai+1*...*Aj

* Recurrence for C(i,j):
    C(i,j)=min(l){C(i,l)+C(l+1,j)+mi-1*ml*mj: i<=l<=j-1}

ChainMultiply(m0,m1,...mn):
    For i=1->n, C(i,i)=0
    For s=1->n-1:
        For i=1->n=s:
            Let j = i + s
            C(i,j)= inf
            For l=i->j-1:
                cur = mi-1*ml*mj+C(i,l)+C(l+1,j)
                if C(i,j)>cur then C(i,j)=cur
    Return (C(1,n))
"""

"""
DP2: Addendom

Practice Problems:
    [DPV] 6.17
          6.18
          6.19
          6.20
          6.7
    
    subproblem: try prefix, then substrings

"""