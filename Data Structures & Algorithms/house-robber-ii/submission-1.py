class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 0:
            return 0
        
        if len(nums) <= 1:
            return max(nums)

        return max(self.rob_aux(nums[1:]), self.rob_aux(nums[:-1]))

    def rob_aux(self, nums: List[int]):
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
    