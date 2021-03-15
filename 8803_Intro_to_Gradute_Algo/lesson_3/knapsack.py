"""
Knapsack Problem
* Input: n 
    integer weights w1, ..., wn
    integer values  v1, ..., vn

    total capacity B

Goal: find subset S of objects that:
    a) fit in backpack -- total weight <= B
    b) maximizes total value


* Variants
two versions:
    1) one copy of each object -- without repetition
    2) unlimited supply -- with repetition

* Greedy algorithm
Ex:
    Object: 1   2   3   4
    Value:  15  10  8   1
    weight: 15  12  10  5

    B = 22

Greedy: sort object by ri = vi/wi=value per unit of weight
    r1>r2>r3>r4

Greedy solution: 1&4 value =16  FAIL!!!!!!

* DP design: attempt 1

Step 1: Define Subproblem
    K(i) = max value achievable using a subset of objects 1,...,i

Step 2: Express K(i) in terms of K(1),..., K(i-1)

* DP design: attempt 2

Step 1: Define Subproblem
    For i & b where 0<=i<=n & 0<=b<=B:
        let k(i,b) = max value achievable using a subset of objects
            1,...,i
            & total weight <=b
    out goal: compute K(n,B)

Step 2: 
    if wi <= b:
        then k(i,b) =  max{vi+K(i-1,b-wi), k(i-1,b)}
        else k(i,b) = k(i-1, b)

    Base case: K(0, b) = 0 & K(i,0) = 0

* Pseudocode
KnapsackNoRepeat(w1,...,wn,r1,...,rn,B):
    for b=0->B: K(0,b)=0
    for i=0->n: K(i,0)=0
    for i=1->n:
        for b=1->B:
            if wi<=b:
                then k(i,b)=max{vi+K(i-1,b-wi), K(i-1,b)}
            else:
                K(i,b)=K(i-1,b)
    Return K(n,B)

total time O(nB)


"""


"""
* Unlimited supply: can use an object as many times as we'd like

* DP design

Step 1: Define Subproblem
K(i,b) = max value achievable using a subset of objects
            1,...,i
            & total weight <=b

Step 2: 
    if wi <= b:
        then k(i,b) =  max{vi+K(i,b-wi), k(i-1,b)}
        else k(i,b) = k(i-1, b)

    Base case: K(0, b) = 0 & K(i,0) = 0
"""

"""
SIMPLER SUBPROBLEM

For b where 0<=b<=B:
    K(b) = max value attainable using weight <= b

Recurrence: try all possiblities for last object to add

K(b) = max(i) {vi + K(b-wi): 1<=i<=n, wi<=b}


pseudocode

KnapsackRepeat(w1,...wn,1,...,vn,B):
    for b = 0 -> B
        K(b) = 0
        for i = 1 -> n:
            if w1 <= b & K(b) < vi + K(b-wi):
                then K(b)=vi + K(b-wi)
    return (K(B))

Running time O(nB)


"""