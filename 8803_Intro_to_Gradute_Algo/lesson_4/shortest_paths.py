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