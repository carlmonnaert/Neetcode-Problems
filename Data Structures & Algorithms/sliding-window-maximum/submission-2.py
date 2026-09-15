from collections import Counter
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums[:k])
        
        left = 0
        right = left + k - 1
        
        m = max( nums[:k] )
        
        l = []
        l.append(m)
        
        while right + 1 < len(nums):
            right += 1
            left += 1
            
            r_n = nums[right]
            l_n = nums[left-1]
            
            c[l_n] -= 1
            c[r_n] = 1 + c.get(r_n, 0)
            
            if c[l_n] != 0:
                m = max(r_n, m)
            else:
                del c[l_n]
                m = max(c.keys())
            l.append(m)
        return l


            