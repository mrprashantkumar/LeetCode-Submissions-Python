class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        d = Counter(hand)
        for _ in range(n // groupSize):
            mini = min(d)
            for k in range(groupSize):
                if d[mini] > 0:
                    d[mini] -= 1
                    if d[mini] == 0:
                        del d[mini]
                    mini += 1
                else:
                    return False
        
        return True