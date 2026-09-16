class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        v = 0
        for i, h in enumerate(heights):
            current_start = i
            while s and s[-1][1] > h:
                j, h2 = s.pop()
                v = max(v, (i-j) * h2 )
                current_start = j
            s.append([current_start,h])
        
        while s:
            i, h = s.pop()
            v = max( (len(heights) - i) * h, v)
        return v