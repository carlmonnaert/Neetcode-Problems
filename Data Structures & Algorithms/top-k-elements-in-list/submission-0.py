class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = { n : 0 for n in nums }
        
        for n in nums:
            h[n] += 1
        
        items = h.items()
        keys = [ key for key,_ in items ]
        vals = [ val for _,val in items ]
        
        l = []
        for i in range(k):
            M = max(vals)
            idx = vals.index(M)
            vals.pop(idx)
            key = keys.pop(idx)
            l.append(key)
        return l