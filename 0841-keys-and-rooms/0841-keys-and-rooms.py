class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        
        qu = deque([0])
        visited[0]=True
        
        while qu:
            curr = qu.popleft()
            for key in rooms[curr]:
                if not visited[key]:
                    visited[key] = True
                    qu.append(key)
        
        return all(visited)
        