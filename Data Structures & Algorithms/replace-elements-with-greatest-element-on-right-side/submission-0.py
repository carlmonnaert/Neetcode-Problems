class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
        ptr = len(arr) - 1
        res = []
        m = -1
        while ptr >= 0:
            res.append(m)
            m = max(m, arr[ptr])
            ptr -= 1
        return res[::-1]
