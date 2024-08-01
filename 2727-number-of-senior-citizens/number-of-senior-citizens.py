class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(i[11:13]) > 60 for i in details)