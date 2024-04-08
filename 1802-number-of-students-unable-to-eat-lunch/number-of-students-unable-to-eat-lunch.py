class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        d = Counter(students)
        n = len(sandwiches)
        i = 0
        while i < n:
            if d[sandwiches[i]] > 0:
                d[sandwiches[i]] -= 1
            else:
                break
            i += 1
        return n-i