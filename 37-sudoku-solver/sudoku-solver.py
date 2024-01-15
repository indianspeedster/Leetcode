class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for ch in [str(c) for c in range(1, 10)]:
                            if isvalid(board, ch, i, j):
                                board[i][j] = ch
                                if dfs(board):
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True
        def isvalid(board, ch, row, col):
            for i in range(9):
                if ch == board[i][col]:
                    return False
                if ch == board[row][i]:
                    return False
                if ch == board[int(3 * (row//3) + i//3)][int(3 * (col//3) + i %3)]:
                    return False
            return True
        dfs(board)
        

            

        