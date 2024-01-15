class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dl={}
        players = set()
        
        for i, j in matches:
            players.add(i)
            players.add(j)
            dl[j] = dl.get(j, 0)+1

        zero_lose, one_lose = [], []
        for player in players:
            count = dl.get(player, 0)
            if count == 0:
                zero_lose.append(player)
            elif count == 1:
                one_lose.append(player)
        
        return [sorted(zero_lose), sorted(one_lose)]