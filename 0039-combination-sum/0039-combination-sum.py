class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(currentList, si, target):
            if target == 0:
                ans.append(currentList)
                return

            for i in range(si, n):
                num = candidates[i]
                if num <= target:
                    helper(currentList+[num], i, target-num)
                else:
                    break
        
        
        n = len(candidates)
        candidates.sort()
        ans = []
        helper([], 0, target)
        return ans