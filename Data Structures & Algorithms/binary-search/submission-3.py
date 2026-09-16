class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left + 1< right :
            mid = int((left + right) / 2)
            n = nums[mid]
            if target < n:
                right = mid

            elif target > n:
                left = mid
            
            else:
                return mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        return -1
