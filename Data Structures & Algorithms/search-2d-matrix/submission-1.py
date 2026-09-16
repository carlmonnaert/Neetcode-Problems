class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix:
            n,m = len(matrix), len(matrix[0])

        left = 0
        right = n * m - 1

        while left + 1 < right:
            mid = int((left + right) / 2)
            n = matrix[ mid // m ][ mid % m]
            if target < n:
                right = mid
            elif target > n:
                left = mid
            else:
                return True
        return matrix[ left // m ][left % m] == target or matrix[ right // m ][right % m] == target