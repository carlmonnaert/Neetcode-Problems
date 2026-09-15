class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        res = 0

        max_f = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_f = max(max_f, count[s[right]])

            if (right -left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res