from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                
                elif s > 0:
                    right -= 1
                
                else:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1

        return list(res)