class LFUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.f = defaultdict(dict)
        self.c = capacity
        self.m = 1
        
    def get(self, key: int) -> int:
        if key not in self.d: return -1
        x = self.d.pop(key)
        v = self.f[x].pop(key)
        if not self.f[x] and self.m == x:
            self.m += 1
        self.f[x+1][key] = v
        self.d[key] = x + 1
        return v
        
    def put(self, key: int, value: int) -> None:
        if self.c <= 0: return
        if key in self.d:
            self.get(key)
            self.f[self.d[key]][key] = value
            return
        
        if len(self.d) >= self.c:
            k = next(iter(self.f[self.m]))
            self.f[self.m].pop(k)
            self.d.pop(k)
            
        self.d[key] = 1
        self.f[1][key] = value
        self.m = 1
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)