class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        def helper(safeness):
            def dfs(p, q):
                if p == n-1 and q == n-1:
                    return True
                
                seen.add((p, q))
                for dp, dq in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= p+dp < n and 0 <= q+dq < n and (p+dp, q+dq) not in seen and dist[p+dp][q+dq] >= safeness:
                        if dfs(p+dp, q+dq):
                            return True
                return False

            seen = set()
            return dfs(0, 0) if dist[0][0] >= safeness else False

        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
        
        qu = deque()
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    qu.append((i, j))
                    visited.add((i, j))
        
        dist = [[-1]*n for _ in range(n)]
        step = 1
        while qu:
            l = len(qu)
            for _ in range(l):
                x, y = qu.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= x+dx < n and 0 <= y+dy < n and (x+dx, y+dy) not in visited and dist[x+dx][y+dy] == -1:
                        dist[x+dx][y+dy] = step
                        qu.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))
            step += 1
        print(dist)
        ans = 0
        low, high = 0, 2*n

        while low <= high:
            mid = (low+high) // 2
            if helper(mid):
                ans = mid
                low = mid+1
            else:
                high = mid-1
        
        return ans