class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        f_max = 0
        count = {}
        answer = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)
            f_max = max(f_max, count[s[right]])
            
            if right - left + 1 > k + f_max:
                count[s[left]] -= 1
                left += 1
            
            else:
                answer = max(answer, right - left + 1)
        return answer