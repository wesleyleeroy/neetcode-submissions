class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        queens = []
        cols = set()
        diag = set()
        anti_diag = set()

        def backtrack(row):
            if row == n:
                board = ['.' * n for _ in range(n)]
                for r, c in enumerate(queens):
                    board[r] = board[r][:c] + 'Q' + board[r][c+1:]
                results.append(board)
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag or (row + col) in anti_diag:
                    continue
                
                queens.append(col)
                cols.add(col)
                diag.add(row - col)
                anti_diag.add(row + col)

                backtrack(row+1)

                queens.pop()
                cols.remove(col)
                diag.remove(row-col)
                anti_diag.remove(row+col)

        backtrack(0)
        return results

                
