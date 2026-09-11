class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = { n : 0 for n in nums }
        for n in nums:
            h[n] += 1
        for n in nums:
            if h[n] > 1:
                return True
        return False