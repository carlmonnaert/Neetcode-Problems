class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ptr = len(s) -1
        while s[ptr] == " ":
            ptr -= 1
        
        end = ptr
        while ptr >= 0 and s[ptr] != " ":
            ptr -= 1

        return end - ptr