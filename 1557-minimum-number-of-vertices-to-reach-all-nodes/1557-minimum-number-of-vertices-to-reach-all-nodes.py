class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # graph = [[] for _ in range(n)]
        # for i, j in edges:
        #     graph[j].append(i)
        # ans = []
        # for i in range(n):
        #     if not graph[i]:
        #         ans.append(i)
        # return ans
        ans = set(range(n))
        for _, e in edges:
            if e in ans:
                ans.remove(e)
        return list(ans)