class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        ca, cb = 0, 0
        i = 0
        n = len(colors)
        
        while i<n:
            c = colors[i]
            count = 0
            while i<n and colors[i] == c:
                i += 1
                count += 1
            
            if c == 'A':
                ca += max(0, count-2)
            else:
                cb += max(0, count-2)
        
        return ca > cb