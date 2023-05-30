class MyHashSet:

    def __init__(self):
        self.arr = [0]*1000007

    def add(self, key: int) -> None:
        if self.arr[key] == 0:
            self.arr[key] += 1

    def remove(self, key: int) -> None:
        if self.arr[key] > 0:
            self.arr[key] -= 1

    def contains(self, key: int) -> bool:
        return self.arr[key] > 0
            


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)