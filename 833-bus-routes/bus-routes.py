class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        largest_route = 0
        for route in routes:
            largest_route = max(max(route), largest_route)

        graph = [[] for i in range(largest_route + 1)]
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].append(i)

        queue = deque([source])
        seen = set()
        seen_routes = set()
        answer = 0
        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                if curr == target:
                    return answer
                seen.add(curr)

                for child in graph[curr]:
                    if child not in seen_routes:
                        seen_routes.add(child)
                        for stop in routes[child]:
                            if stop not in seen:
                                queue.append(stop)
            answer += 1
        return -1