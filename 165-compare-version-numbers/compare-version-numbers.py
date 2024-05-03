class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]

        for x, y in zip_longest(v1, v2, fillvalue = 0):
            if x > y:
                return 1
            if x < y:
                return -1
        
        return 0