class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def isWinner(player):
            for i in range(3):
                if board[i][0] == board[i][1] == board[i][2] == player:
                    return True                        

            for i in range(3):
                if board[0][i] == board[1][i] == board[2][i] == player:
                    return True 

            if (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
                return True
            
            return False
        
        cx, co = 0, 0
        for row in board:
            for i in row:
                if i == 'X':
                    cx += 1
                elif i == 'O':
                    co += 1
                
        if co > cx or cx-co > 1:
            return False
        
        if isWinner('O'):
            if isWinner('X'):
                return False
            return cx == co
        
        if isWinner('X') and cx-co != 1:
            return False
        
        return True