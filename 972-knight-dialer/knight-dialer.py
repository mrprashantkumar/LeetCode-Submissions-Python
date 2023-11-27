class Solution:
    def knightDialer(self, n: int) -> int:
        d = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4]}
        qu = Counter()
        for i in range(10):
            qu[i] = 1

        ans = 10
        for _ in range(n-1):
            ans = 0
            newqu = Counter()
            for curr in qu:
                ans += qu[curr]*len(d[curr])
                for nxt in d[curr]:
                    newqu[nxt] += qu[curr]
            ans %= 1000000007
            qu = newqu
        return ans