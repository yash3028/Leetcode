class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        # we will sort the array in descending order so that we can expensive comes first
        cost.sort(reverse=True)
        total = 0
        l = len(cost)
        # every time third one is cheaper, so we will get for skip that index
        for i in range(0, l, 3):
            total += cost[i]
            if i + 1 < l:
                total += cost[i + 1]
        return total
    
ans = Solution().minimumCost([1,2,3])
print(ans)