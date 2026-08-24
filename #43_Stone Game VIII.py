from functools import lru_cache
from typing import List


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0]*n
        prefix[0]=stones[0]
        for i in range(1,n):
            prefix[i] = stones[i]+prefix[i-1]

        @lru_cache(None)
        def solve(i):
            if i==n-1:
                return prefix[n-1]

            take = prefix[i] - solve(i+1)
            skip = solve(i+1)
            return max(take,skip)
        return solve(1)
ans  = Solution().stoneGameVIII([-1,2,-3,4,-5])
print(ans)