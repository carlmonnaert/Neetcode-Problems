class Solution:

    def numDecodings(self, s: str) -> int:
        # 1111 -> at each step, two ways to decode f(n) = f(n+1) + f(n+2)  
        # 1011 -> at step one, we must decompose as 2 digits f(1) = f(2)
        # 7111 -> at step one, forced to decompose as single digit f(1) = f(2)
        # 1001 -> can not be decoded past step 2
        # f(n) is the number of ways to decompose the n last elements
        # f(n) = f(n+1)1_{no zero in n} + f(n+2)1_{the two following form a valid}

        def mult_1(x):
            return 1 if int(x) != 0 else 0

        def mult_2(x,y):
            return 1 if int(x) == 1 or (int(x) == 2 and int(y) <= 6) else 0

        n = len(s)
        if n == 0:
            return 1

        if n == 1:
            return 1 if int(s) != 0 else 0
        
        res = [1 for i in range(n+2)]
        res[-1] = 1
        i = len(s) - 1
        while i >= 0:
            multiplier_1 = mult_1(s[i])
            multiplier_2 = 0 if i == len(s) - 1 else mult_2(s[i], s[i+1])
            res[i] = multiplier_1 * res[i+1] + multiplier_2 * res[i+2]
            i -= 1
        return res[0]
