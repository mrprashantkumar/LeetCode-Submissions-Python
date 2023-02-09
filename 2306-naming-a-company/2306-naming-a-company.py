class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        group = defaultdict(set)
        for word in ideas:
            group[word[0]].add(hash(word[1:]))
        
        ans = 0
        for a, vala in group.items():
            for b, valb in group.items():
                same = len(vala & valb)
                ans += (len(vala) - same) * (len(valb) - same)
        
        return ans