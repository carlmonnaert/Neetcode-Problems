from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])
        
        if c1 == c2:
            return True
        
        for i in range(len(s2) - len(s1)):
            left = s2[i]
            right = s2[i+len(s1)]
            c2[left] -= 1
            if c2[left] == 0:
                del c2[left]
            c2[right] += 1
            if c1 == c2:
                return True
        return False
