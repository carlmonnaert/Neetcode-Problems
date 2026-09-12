class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        N = len(nums)
        nums = set(nums)
        if N <= 1:
            return N
        
        starters = [x for x in nums if x-1 not in nums]
        lens = { s : 1 for s in starters }
        
        for s in starters:
            nex = s + 1
            while nex in nums:
                nex += 1
            lens[s] = nex - s
        return max(lens.values())
            