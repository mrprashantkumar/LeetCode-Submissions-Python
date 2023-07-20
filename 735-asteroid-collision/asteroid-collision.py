class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        seen = []
        seen.append(asteroids[0])
        for right in asteroids[1:]:
            if right<0:
                while seen and seen[-1]>0:
                    left = seen.pop()
                    if abs(right)<left:
                        seen.append(left)
                        break
                    elif abs(right)==left:
                        break
                else:
                    seen.append(right)
            else:
                seen.append(right)
        return seen