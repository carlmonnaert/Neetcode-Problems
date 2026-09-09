class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for n in nums]
        
        p = 1
        for i,n in enumerate(nums):
            res[i] *= p
            p *= n
        
        s = 1
        nums.reverse()
        for i,n in enumerate(nums):
            res[-i-1] *= s
            s *= n
        
        return res 