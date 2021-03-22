"""
Practice Problems: 6.1, 6.2, 6.3, 6.4, 6.11

Approach
1. Define subproblem
    a. prefix
    b. add constrain

2. Recurrence relation
    T(i) in terms of T(1),...T(i-1)
"""

"""
Input a1, ... an

Goal Substring with max sum

subproblem for 0<=i<=n

    let S(i) = max sum from substring of a1, ..., ai, which include ai

    S(i) = ai + max{0, S(i-1)}

Output: max(S(i))


"""