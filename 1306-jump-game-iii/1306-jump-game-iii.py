class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        qu = deque([start])
        visited = set()
        visited.add(start)
        while qu:
            curr = qu.popleft()
            if arr[curr] == 0:
                return True
            if curr+arr[curr] < n and curr+arr[curr] not in visited:
                qu.append(curr+arr[curr])
                visited.add(curr+arr[curr])
            if curr-arr[curr] >= 0 and curr-arr[curr] not in visited:
                qu.append(curr-arr[curr])
                visited.add(curr-arr[curr])
        
        return False