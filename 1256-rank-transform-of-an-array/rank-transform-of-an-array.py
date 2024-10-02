class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}
        curr_rank = 1
        for ele in sorted(set(arr)):
            ranks[ele] = ranks.get(ele, curr_rank)
            curr_rank += 1
        
        ans = []
        for ele in arr:
            ans.append(ranks[ele])
        return ans