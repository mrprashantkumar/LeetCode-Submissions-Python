class AllOne:

    def __init__(self):
        self.freq = {}
    
    def inc(self, key: str) -> None:
        self.freq[key] = self.freq.get(key, 0) + 1
        
    def dec(self, key: str) -> None:
        self.freq[key] = self.freq.get(key, 0) - 1
        if self.freq[key] == 0:
            del self.freq[key]

    def getMaxKey(self) -> str:
        count, res = 0, ""
        for k, v in self.freq.items():
            if v > count:
                count = v
                res = k
        return res

    def getMinKey(self) -> str:
        count, res = inf, ""
        for k, v in self.freq.items():
            if v < count:
                count = v
                res = k
        return res


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()