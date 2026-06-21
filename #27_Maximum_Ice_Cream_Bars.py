from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # we will sort to maximise the number of ice cream bars
        costs.sort()
        total = 0
        for i in range(len(costs)):
            # we will buy if coins are greater than cost of ice cream
            if coins>=costs[i]:
                total+=1
                coins-=costs[i]
        return total

ans = Solution().maxIceCream([1,3,2,4,1],7)
print(ans)