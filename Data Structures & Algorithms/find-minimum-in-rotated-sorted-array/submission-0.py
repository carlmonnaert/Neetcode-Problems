class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        left = 0
        right = n-1
        m = nums[0]
        while left < right - 1 :
            p = (left + right) // 2
            pointed = nums[p]
            if pointed < m:
                right = p
            elif pointed > m:
                left = p
        return min(nums[right],  m)