class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        fn1, fn = 1, 2
        for i in range(2, n):
            aux = fn
            fn = fn + fn1
            fn1 = aux
        return fn 
