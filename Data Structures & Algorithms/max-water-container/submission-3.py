class Solution:        
    def maxArea(self, heights: List[int]) -> int:
        
        # Brute force:
        # h = {(i,j) : 0 for i in range(len(heights)) for j in range(len(heights))}
        # for i,j in h.keys():
        #     h[(i,j)] = min(heights[i], heights[j]) * abs(i - j)
        # return max(h.values())

        start = 0
        end = len(heights) - 1
        M = min(heights[start], heights[end]) * (end - start)
        while start < end:
            if M < min(heights[start], heights[end]) * (end - start):
                M = min(heights[start], heights[end]) * (end - start)
            
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return M