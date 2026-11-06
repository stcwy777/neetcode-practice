class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)

        l, r = 0, n - 1

        res = 0
        while l < r:
            res += 1
            if people[l] + people[r] > limit:
                r -= 1
            else:
                l += 1
                r -= 1
        if l == r:    
            res += 1
        
        return res