class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def helper(i, degree, count):
            if i >= m:
                if all(val == 0 for val in degree):
                    self.ans = max(self.ans, count)
                
                return
            
            degree[requests[i][0]] += 1
            degree[requests[i][1]] -= 1

            helper(i+1, degree, count+1)

            degree[requests[i][0]] -= 1
            degree[requests[i][1]] += 1

            helper(i+1, degree, count)
        
        m = len(requests)
        degree = [0]*n
        self.ans = 0
        helper(0, degree, 0)
        return self.ans