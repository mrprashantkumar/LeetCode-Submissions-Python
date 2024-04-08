class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        qu = deque([i for i in students])
        sandwiches.reverse()
        ans = 0
        curr = 0
        i = 0
        while qu and curr < n:
            stu = qu.popleft()
            if stu == sandwiches[-1]:
                sandwiches.pop()
                ans += 1
                curr = 0
            else:
                curr += 1
                qu.append(stu)
            
        return n - ans