class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1, h2 = {c : 0 for c in s} , {c : 0 for c in t}
        if h1.keys() != h2.keys():
            return False
        for c in s:
            h1[c] += 1
        for c in t:
            h1[c] -= 1
        for v in h1.values():
            if v != 0:
                return False
        return True