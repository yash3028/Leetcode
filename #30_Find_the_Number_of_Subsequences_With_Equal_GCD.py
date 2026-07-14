from functools import lru_cache
from math import gcd
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        # cache is used because if a same subarray is appeared we dont need to calcualte again
        @lru_cache(None)
        def dfs(i, s1, s2):
            if i == n:
                return 1 if s1 > 0 and s1 == s2 else 0

            # Skip nums[i]
            ans = dfs(i + 1, s1, s2)

            # Put ele in first subsequence
            ans += dfs(i + 1, gcd(s1, nums[i]), s2)

            # Put ele in second subsequence
            ans += dfs(i + 1, s1, gcd(s2, nums[i]))

            return ans % MOD

        return dfs(0, 0, 0)
    
ans = Solution().subsequencePairCount([1,2,3,4])
print(ans)