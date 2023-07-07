class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        countT, countF = 0, 0
        left, right = 0, 0
        ans = 0
        while right < n:
            if min(countT, countF) > k:
                while min(countT, countF) > k:
                    if answerKey[left] == 'T':
                        countT -= 1
                    else:
                        countF -= 1
                    left += 1
                ans = max(ans, countT+countF)
            else:
                ans = max(ans, countT+countF)
                if answerKey[right] == 'T':
                    countT += 1
                else:
                    countF += 1
                right += 1
            
            # print(left, right, countT, countF, ans)
        
        while min(countT, countF) > k:
            if answerKey[left] == 'T':
                countT -= 1
            else:
                countF -= 1
            left += 1
        ans = max(ans, countT+countF)
        return ans