class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def helper(i):
            if i >= n:
                return 0
            
            res = inf
            currWidth, currHeight = 0, 0
            put = 0
            for j in range(i, n):
                if currWidth + books[j][0] <= shelfWidth:
                    currWidth += books[j][0]
                    currHeight = max(currHeight, books[j][1])
                    put = helper(j+1)
                else:
                    break
                res = min(res, currHeight + put)
            return res

        n = len(books)
        return helper(0)