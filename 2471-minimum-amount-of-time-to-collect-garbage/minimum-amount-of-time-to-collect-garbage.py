class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def getlast(arr,n, x):
            for i in range(n-1, -1, -1):
                if x in arr[i]:
                    return i
            return 0
        
        ans=0
        n = len(garbage)
        g = getlast(garbage, n, "G")
        p = getlast(garbage, n, "P")
        m = getlast(garbage, n, "M")
        for i in garbage:
            if "G" in i:
                ans += (i.count("G"))
            if "P" in i:
                ans += (i.count("P"))
            if "M" in i:
                ans += (i.count("M"))
        
        ans += sum(travel[:g])
        ans += sum(travel[:p])
        ans += sum(travel[:m])
        return ans