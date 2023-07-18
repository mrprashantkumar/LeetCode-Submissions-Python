class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isvalid(val, x, y):
            for a in range(9):
                if board[a][y] == val:
                    return False
            
                if board[x][a] == val:
                    return False
                
                if board[3*(x//3) + (a//3)][3*(y//3) + (a%3)] == val:
                    return False
            return True

        def helper(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in range(1, 10):
                            if isvalid(str(num), i, j):
                                board[i][j] = str(num)
                                if helper(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False
            return True
        
        helper(board)