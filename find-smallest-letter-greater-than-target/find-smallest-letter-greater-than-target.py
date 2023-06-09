class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        ans = bisect.bisect_right(letters, target)
        if ans == n:
            return letters[0]
        return letters[ans]