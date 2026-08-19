from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        mp = {}
        #finding which seats are booked in a row
        for reservedSeat in reservedSeats:
            row = reservedSeat[0]
            seat = reservedSeat[1]

            if row not in mp:
                mp[row] = set()

            mp[row].add(seat)
        #if a row has no seat booked we can have maximum of two families in a row
        result = (n - len(mp)) * 2

        for row, bookedSeats in mp.items():
            def isAvailable(seat):
                return seat not in bookedSeats
            #checking if any seat of groupA, groupB or groupC is booked 
            groupA = (isAvailable(2) and isAvailable(3) and isAvailable(4) and isAvailable(5))

            groupB = (isAvailable(4) and isAvailable(5) and isAvailable(6) and isAvailable(7))

            groupC = (isAvailable(6) and isAvailable(7) and isAvailable(8) and isAvailable(9))
            #if no is booked in A or C then we can have two groups in that row
            if groupA and groupC:
                result += 2
            elif groupA or groupB or groupC:
                result += 1

        return result
ans = Solution().maxNumberOfFamilies(3,[[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]])
print(ans)