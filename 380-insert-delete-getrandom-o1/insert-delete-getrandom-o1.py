class RandomizedSet:

    def __init__(self):
        self.d = {}

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        
        self.d[val] = 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        
        del self.d[val]
        return True

    def getRandom(self) -> int:
        return random.choice(list(self.d.keys()))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()