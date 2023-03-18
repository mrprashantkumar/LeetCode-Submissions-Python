class BrowserHistory:

    def __init__(self, homepage: str):
        self.nums1 = []
        self.nums2 = []
        self.ans = homepage

    def visit(self, url: str) -> None:
        self.nums1.append(self.ans)
        self.nums2 = []
        self.ans = url

    def back(self, steps: int) -> str:
        while steps and self.nums1:
            self.nums2.append(self.ans)
            self.ans = self.nums1.pop()
            steps -= 1
        return self.ans

    def forward(self, steps: int) -> str:
        while steps and self.nums2:
            self.nums1.append(self.ans)
            self.ans = self.nums2.pop()
            steps -= 1
        return self.ans
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)