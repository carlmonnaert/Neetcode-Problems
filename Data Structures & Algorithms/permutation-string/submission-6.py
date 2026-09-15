from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        fitted_letters = 0
        h1 = Counter(s1)
        h2 = Counter(s2[:len(s1)])

        if h1 == h2:
            return True
        
        for i in range(len(s1), len(s2)):
            new_char = s2[i]
            h2[new_char] += 1

            left_char = s2[i - len(s1)]
            h2[left_char] -= 1

            if h2[left_char] == 0:
                del h2[left_char]

            if h1 == h2:
                return True
        return False