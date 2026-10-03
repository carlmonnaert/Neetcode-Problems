class Solution:
    def search(self, nums: List[int], target: int) -> int:
        id_min = self.find_min(nums)
        n = len(nums)
        sorted_nums = nums[id_min:] + nums[:id_min]
        print(sorted_nums)
        l, r = 0, n - 1
        while l <= r:
            p = (l + r) // 2
            num = sorted_nums[p]
            if num < target:
                l = p + 1
            
            elif num == target:
                return (p + id_min) % n
            
            else:
                r = p - 1
        return -1

    def find_min(self, nums):
        n = len(nums)
        l, r = 0, n-1
        m = nums[0]
        id_m = 0
        while l <= r:
            p = (l + r) // 2
            if nums[p] < nums[0]:
                if nums[p] < m:
                    m = nums[p]
                    id_m = p
                    r = p - 1
                
            else :
                l = p + 1
        return id_m