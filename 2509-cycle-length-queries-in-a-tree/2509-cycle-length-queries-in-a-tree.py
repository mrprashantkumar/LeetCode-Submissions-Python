class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        for a, b in queries:
            count = 0
            while a != b:
                if a > b:
                    a //= 2
                else:
                    b //= 2
                    
                count += 1

            ans.append(count+1)
        
        return ans