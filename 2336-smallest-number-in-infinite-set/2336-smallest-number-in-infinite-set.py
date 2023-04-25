class SmallestInfiniteSet:

    def __init__(self):
        self.arr = [int(i) for i in range(1, 1001)]
        heapq.heapify(self.arr)

    def popSmallest(self) -> int:
        return heapq.heappop(self.arr)

    def addBack(self, num: int) -> None:
        if num not in set(self.arr):
            heapq.heappush(self.arr, num)
            


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)