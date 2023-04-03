class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        low, high = 0, len(people)-1
        ans = 0
        
        while low <= high:
            if people[low]+people[high] <= limit:
                low+=1
            high-=1
            ans+=1
        return ans
        