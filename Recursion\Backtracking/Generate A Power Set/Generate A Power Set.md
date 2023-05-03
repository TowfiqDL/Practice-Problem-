##**Generate A Power Set** 

##The power set of a set S is the set of all subsets of S, includingboth the empty set 0 and S itself.Write a function that takes as input a set and retums its power set.
##For example:: sets = {1, 2, 3} power_set = {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}


##**Time Complexity and Space Complexity**
The number of recursive calls, C(n) satisfies the recurrence C(n) = 2C(n - 1), which solves to C(n) = O(2"). Since we spend O(n) time within a call, the time complexity is O(n2n). The space complexity is O(n2"), since there are 2ft subsets, and the average subset size is nlz. If we just want to print the subsets, rather than retuming all of them, we simply perform a print instead of adding the subset to the result, which reduces the space complexity to O(n)-the time complexity remains the same.

