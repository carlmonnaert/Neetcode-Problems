class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_s = [ ord(c) for c in s ]
        score_diffs = [ abs(ascii_s[i] - ascii_s[i+1]) for i in range(len(s)-1) ]
        score = sum(score_diffs)
        return score