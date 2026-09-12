class Solution:
    def isPalindrome(self, s: str) -> bool:
        def aux(s1):
            if len(s1) <= 1:
                return True
            else:
                return (s1[0] == s1[-1]) and aux(s1[1:-1])
        s = s.lower()
        s = [c for c in s if (ord('a') <= ord(c) and ord(c) <= ord('z')) or (ord('0') <= ord(c) and ord(c) <= ord('9'))]
        s = ''.join(s)
        return aux(s)