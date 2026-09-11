import numpy as np
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = np.argsort(nums)
        i,j = 0, len(nums)-1
        while i < j:
            s = nums[idx[i]] + nums[idx[j]]
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                l = [idx[i], idx[j]]
                l.sort()
                return l