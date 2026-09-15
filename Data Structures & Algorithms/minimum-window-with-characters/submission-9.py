from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or len(s) == 0:
            return ""
        
        target = Counter(t)
        n_target = len(target.keys())

        seen = { c : 0 for c in target.keys() }
        n_seen = 0

        left = 0
        right = 0

        res = None
        M = None

        while left <= right and right < len(s):
            c = s[right]
            
            if c in target.keys():
                seen[c] += 1
                if seen[c] == target[c]:
                    n_seen += 1

            while n_seen == n_target and left <= right:
                if M is None or M > right - left + 1:
                    M = right - left + 1
                    res = left, right
                left = left + 1
                l_char = s[left - 1]
                if l_char in target.keys():
                    seen[l_char] -= 1
                    if seen[l_char] < target[l_char]:
                        n_seen -= 1
            right += 1
        
        return "" if res is None else s[res[0]: res[1]+1] 