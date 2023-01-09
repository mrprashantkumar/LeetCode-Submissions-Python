class MinStack:

    def __init__(self):
        self.nums = []
        self.mini = 100000000007

    def push(self, val: int) -> None:
        if self.mini == None:
            self.nums.append([val, val])
        if self.mini <= val:
            self.nums.append([val, self.mini])
        else:
            self.mini = val
            self.nums.append([val, val])

    def pop(self) -> None:
        self.nums.pop()
        if self.nums:
            self.mini = self.nums[-1][1]
        else:
            self.mini = 100000000007

    def top(self) -> int:
        return self.nums[-1][0]

    def getMin(self) -> int:
        
        return self.nums[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()