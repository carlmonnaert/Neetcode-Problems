class Solution:
    def rob(self, nums: List[int]) -> int:
        # Go from the left, at each step I either rob the first, or the second.
        # gain(i) = what I can gain by stealing up to i
        n = len(nums)
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        l = [0 for i in range(n+2)]
        ptr = n-1
        while ptr >= 0:
            l[ptr] = max(l[ptr+1], l[ptr+2] + nums[ptr])
            ptr -= 1
        return l[0]
