from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            # Optimization: If the current smallest number is > 0, 
            # no three numbers can sum to 0.
            if nums[i] > 0:
                break
                
            # Skip duplicates for the first number to ensure unique triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    # Append the VALUES, not the indices
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return res