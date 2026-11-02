class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for mid in range(len(s)):
            i = 0
            while 0 <= mid - i and mid + i < n and s[mid - i] == s[mid + i]:
                res += 1
                i += 1
            
            i = 0
            while 0 <= mid - i and mid + i + 1< n and s[mid - i] == s[mid + i + 1]:
                res += 1
                i += 1
        return res