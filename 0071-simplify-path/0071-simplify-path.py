class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        
        for i in path.split("/"):
            if ans and i == "..":
                ans.pop()
            elif i not in [".", "", ".."]:
                ans.append(i)
        
        return "/" + "/".join(ans)