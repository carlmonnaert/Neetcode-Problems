class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left = [ 0 for i in range(N) ]
        right = [ 0 for i in range(N) ]
        for i in range(1,N):
            left[i] = max( height[i-1] , left[i-1] )
        for i in range(N-2,-1, -1):
            right[i] = max( height[i+1], right[i+1] )
        heights = [ min(left[i], right[i]) - height[i] if min(left[i], right[i]) - height[i] > 0 else 0 for i in range(N-1) ]
        return sum(heights)