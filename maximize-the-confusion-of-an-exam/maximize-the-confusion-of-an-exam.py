class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        countT, countF = 0, 0
        left, right = 0, 0
        ans = 0
        for right in range(n):
            if answerKey[right] == 'T':
                countT += 1
            else:
                countF += 1

            while min(countT, countF) > k:
                if answerKey[left] == 'T':
                    countT -= 1
                else:
                    countF -= 1
                left += 1

            ans = max(ans, countT+countF)
        return ans