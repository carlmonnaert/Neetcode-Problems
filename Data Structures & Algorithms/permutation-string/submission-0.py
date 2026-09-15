class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        fitted_letters = 0
        h1 = { c : 0 for c in s1}
        for c in s1 :
            h1[c] += 1

        while right < len(s2):
            for c in s2[left: right + 1]:
                n = h1.get(c,None)
                
                if n is not None and h1[c] > 0:
                    h1[c] -= 1
                    fitted_letters += 1
                
                else:
                    fitted_letters = 0
                    h1 = { c : 0 for c in s1}
                    for c in s1 :
                        h1[c] += 1
                    break
            
            if fitted_letters == len(s1):
                return True
            left += 1
            right += 1
        return False