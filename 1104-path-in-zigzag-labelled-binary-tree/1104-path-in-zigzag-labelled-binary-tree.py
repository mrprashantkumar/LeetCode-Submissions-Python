class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = []
        temp = label
        
        level = 0
        while temp:
            temp //= 2
            level += 1
        
        while level:
            ans.append(label)
            maxi = pow(2, level) - 1
            mini = pow(2, level -1) 
            label = (maxi+mini-label)//2
            level -= 1
        
        return ans[::-1]