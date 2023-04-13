class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        
        qu = deque([0])
        visited.add(0)
        
        while qu:
            curr = qu.popleft()
            for key in rooms[curr]:
                if key not in visited:
                    visited.add(key)
                    qu.append(key)
        
        return len(visited) == n