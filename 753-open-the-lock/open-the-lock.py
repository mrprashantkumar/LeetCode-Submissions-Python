class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        if target == '0000':
            return 0

        deadends = set(deadends)
        qu = deque()
        seen = set()

        qu.append('0000')
        seen.add('0000')

        step = 0
        while qu:
            l = len(qu)
            for _ in range(l):
                curr = qu.popleft()

                for i in range(4):
                    ele = curr[i]
                    prev = chr(ord(ele) - 1) if ele != '0' else '9'
                    before = curr[:i] + prev + curr[i+1:]

                    if before == target:
                        return step + 1
                    elif before not in deadends and before not in seen:
                        qu.append(before)
                        seen.add(before)

                    nextt = chr(ord(ele) + 1) if ele != '9' else '0'
                    after = curr[:i] + nextt + curr[i+1:]

                    if after == target:
                        return step + 1
                    elif after not in deadends and after not in seen:
                        qu.append(after)
                        seen.add(after)
            
            step += 1
        
        return -1