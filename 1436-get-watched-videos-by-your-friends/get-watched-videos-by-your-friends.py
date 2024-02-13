class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        qu = deque()
        qu.append(id)
        visited = set()
        visited.add(id)
        
        while qu and level:
            level -= 1
            l = len(qu)
            for _ in range(l):
                curr = qu.popleft()
                for nei in friends[curr]:
                    if nei not in visited:
                        qu.append(nei)
                        visited.add(nei)
        
        d = Counter()
        for i in qu:
            d += Counter(watchedVideos[i])
                
        return sorted(d, key = lambda x :(d[x], x))