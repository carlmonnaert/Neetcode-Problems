class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n0 = nums[0]
        if len(nums) == 1:
            return n0
        max_pos, max_neg = 1, 1
        res = nums[0]
        for i in range(len(nums)):
            aux = max_pos
            max_pos = max([max_pos * nums[i], nums[i], max_neg * nums[i]])
            max_neg = min([aux * nums[i], nums[i], max_neg * nums[i]])
            res = max(res, max_pos)
        return res