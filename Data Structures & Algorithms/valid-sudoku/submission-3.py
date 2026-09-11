class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            h1 , h2 = {str(i+1) : 0 for i in range(9)} , {str(i+1) : 0 for i in range(9)}
            for j in range(9):
                n_vert = board[i][j]
                n_hori = board[j][i]
                
                if n_vert != ".":
                    h1[n_vert] += 1
                
                if n_hori != ".":
                    h2[n_hori] += 1

            m1, m2 = max( h1.values() ), max( h2.values() )
            if m1 > 1 or m2 > 1:
                return False
        
        for i in range(3):
            for j in range(3):
                h = { str(k+1) : 0 for k in range(9) }
                for k in range(9):
                    n = board[i*3 + (k // 3)][3 * j + (k % 3)]
                    if n != ".":
                        h[n] += 1
                m = max( h.values() )
                if m > 1:
                    return False
        return True
