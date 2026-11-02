class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        m = 0
        res = ""
        for mid in range(n):
            i = 0
            while mid - i >= 0 and mid + i < n and s[mid-i] == s[mid+i]:
                if m < 1 + 2*i:
                    m = 1 + 2*i
                    res = s[mid-i : mid+i+1]
                i += 1

        for mid in range(n-1):        
            i = 0
            while mid - i >= 0 and mid + i + 1 < n and s[mid-i] == s[mid+1+i]:
                if m <  2 + 2*i:
                    m = 2 + 2*i
                    res = s[mid-i : mid+i+2]
                i += 1
        return res