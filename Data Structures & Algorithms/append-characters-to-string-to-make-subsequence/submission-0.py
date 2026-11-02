class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Find the biggest subsequence
        common = 0
        pointer_s = 0
        pointer_t = 0
        while pointer_s < len(s) and pointer_t < len(t):
            cs, ct = s[pointer_s], t[pointer_t]
            if cs == ct:
                pointer_s += 1
                pointer_t += 1
            else:
                pointer_s += 1
            
        biggest_sub_size = pointer_t
        # Compute the number of characters missing
        return len(t) - biggest_sub_size
