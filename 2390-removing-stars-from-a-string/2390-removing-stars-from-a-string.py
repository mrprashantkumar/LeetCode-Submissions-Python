class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        for i in s:
            if i != "*":
                ans.append(i)
            else:
                ans.pop()
        return "".join(ans)