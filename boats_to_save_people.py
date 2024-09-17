class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l , r = 0 , len(people)-1
        boat = 0
        people.sort()

        while l <= r:
            if people[l] + people[r] <= limit:
                boat += 1
                l += 1
                r -= 1
            else :
                boat += 1
                r -= 1
        return boat
