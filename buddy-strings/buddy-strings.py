class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s == goal:
            d = Counter(s)
            for val in d.values():
                if val >= 2:
                    return True
            return False

        n, m = len(s), len(goal)
        if n != m:
            return False
        
        fir, sec = -1, -1
        for i in range(n):
            if s[i] != goal[i]:
                if fir == -1:
                    fir = i
                elif sec == -1:
                    sec = i
                else:
                    return False
        if sec == -1:
            return False
        return s[fir] == goal[sec] and s[sec] == goal[fir]
