class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0]*n
        rooms = [i for i in range(n)] # available rooms
        used = []

        for x, y in meetings:
            while used and x >= used[0][0]:
                r = heappop(used)[1]
                heappush(rooms, r)
            
            if not rooms:
                end, r = heappop(used)
                y = end + (y-x)
                heappush(rooms, r)
            
            r = heappop(rooms)
            heappush(used, (y, r))
            count[r] += 1

        maxi = max(count)
        for i, x in enumerate(count):
            if x == maxi:
                return i