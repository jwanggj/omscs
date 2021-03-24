"""
DP: single - source

Given G-> with edge weight & S (E) V
    - assume no negative weight cycles

shortest path P from s to z visits every vertex <= 1
    |P| <= n-1 edges

DP idea: use i=0->n-1 edges on the paths

For 0 <=i <=n-1 & z (E) V:
    let D(i, z) = length of shortest path from s to z using <= i edges

* Recurrence
base case: D(0,S) = 0 & fro all z != S, D(0,z)=inf
For i>=1: look at shortest path s -> z using i edges

    s -> y -> z
     i-1   last edge 

D(i,z)=min{D(i-1,z), min(y){D(i-1,y)+w(y,z)}}

* Pseudocode
Bellman-Ford(G,S,w)
    for all z (E) V, D(0,z)=inf
    D(0,s) = 0
    for i=1->n-1
        for all z (E) V:
            D(i,z) = D(i-1, z)
            for all y->z (E) E:
                if D(i,z) > D(i-1,y) + w(y,z)
                    then D(i,z)=D(i-1,y) + w(y,z)
    return (D(n-1,0))

O(mn)

* Finding Negative Wt Cycle
check if D(n,z) < D(n-1,z)
    for some z (E) V
    
"""

"""
All-pairs shortest path

Bellman-ford idea: conditon on #of edges
New idea: let V= {1,2,3,...,n}
            condition on intermediate vertices
                        => use prefix of V

For 0<=i<=n & 1<=s,t<=n
    let D(i,s,t)=length of shortest path s~t
                    using a subset of {1,...,i}
                    as intermediate vertices

Base case: D(0,s,t) = 
    if st (E) E: w(s,t)
    else: inf

Fpr i >= : look at shortest path p s~t using {1,...,i}
    if i (not E) P: D(i,s,t)=D(i-1,s,t)
    if i (E) P: D(i,s,t)=D(i-1,s,i)+D(i-1,i,t)

    D(i,s,t)=min{D(i-1,s,t), D(i-1,s,i)+D(i-1,i,t)}

Floyd-warshall(G,w):
    For S=1->n:
        For t=1->n:
            if st (E) E then D(0,s,t)=w(s,t)
                        else D(0,s,t)=inf
    For i=1->n:
        For s=1->n:
            For t=1->n:
                D(i,s,t)=min{D(i-1,s,t), D(i-1,s,i)+D(i-1,i,t)}
    return (D(n,.,.))

assume NO negative weight cycles

HW problem:
[DPV] 4.21
"""