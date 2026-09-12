class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {c : 0 for c in s}
        max_len, current_len, start = 0, 0, 0
        
        for i, c in enumerate(s):
            h[c] += 1
            current_len += 1
            
            if h[c] == 1:
                if current_len > max_len:
                    max_len = current_len
            
            else:
                new_start = start
                for r in s[ start : i]:
                    h[r] -= 1
                    current_len -= 1
                    new_start += 1
                    if r == c:
                        break
                start = new_start
        
        return max_len