from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            T = sum([ ceil(p/mid) for p in piles ])
            if T <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left