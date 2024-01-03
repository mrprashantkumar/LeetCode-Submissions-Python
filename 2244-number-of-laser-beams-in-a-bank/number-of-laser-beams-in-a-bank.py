class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        last = 0
        for row in bank:
            count = row.count('1')
            if last > 0:
                if count > 0:
                    ans += last * count
                    last = count
            else:
                last = count
        return ans