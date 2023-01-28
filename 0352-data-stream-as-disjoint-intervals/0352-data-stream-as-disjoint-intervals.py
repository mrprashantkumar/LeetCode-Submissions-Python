class SummaryRanges:

    def __init__(self):
        self.start={}
        self.end={}
        self.visited=set()

    def addNum(self, val: int) -> None:
        if val in self.visited:
            return
        
        self.visited.add(val)
        
        start,end=val,val
        if val+1 in self.start:
            end=self.start[val+1][1]
            self.start.pop(val+1)
        if val-1 in self.end:
            start=self.end[val-1][0]
            self.end.pop(val-1)
            
        self.start[start]=[start,end]
        self.end[end]=[start,end]
        
    def getIntervals(self) -> List[List[int]]:
        return sorted(self.start.values())

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()