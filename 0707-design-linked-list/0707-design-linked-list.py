class MyLinkedList:

    def __init__(self):
        self.nums = []
        self.n = 0

    def get(self, index: int) -> int:
        # print(self.nums)
        if index<self.n:
            return self.nums[index]
        return -1

    def addAtHead(self, val: int) -> None:
        self.nums.insert(0, val)
        self.n += 1
        

    def addAtTail(self, val: int) -> None:
        self.nums.append(val)
        self.n += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        # print(self.nums)
        if index<=self.n:
            self.nums.insert(index, val)
            self.n += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index<self.n:
            self.nums.pop(index)
            self.n -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)