class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        def getstart(x):
            low, high = 0, n-1

            res = 0
            while low <= high:
                mid = (low+high) // 2

                if plates[mid] == x:
                    return mid
                elif plates[mid] > x:
                    res = mid
                    high = mid-1
                else:
                    low = mid+1
            return res

        def getend(x):
            low, high = 0, n-1

            res = n
            while low <= high:
                mid = (low+high)//2
                if plates[mid] == x:
                    return mid
                elif plates[mid] < x:
                    res = mid
                    low = mid+1
                else:
                    high = mid-1
            return res

        plates = []
        for i, x in enumerate(s):
            if x == '|':
                plates.append(i)
        
        n = len(plates)
        # print(plates, n)

        ans = []
        for x, y in queries:
            start = getstart(x)
            end = getend(y)

            if start >= end or x >= y:
                ans.append(0)
            else:
                v = plates[end] - plates[start] -1 - (end-start-1)
                ans.append(v)

        return ans