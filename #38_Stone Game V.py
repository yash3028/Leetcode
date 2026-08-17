from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
        def dfs(l: int, r: int) -> int:
            if l == r:
                return 0

            ans = 0
            for k in range(l, r):
                left = prefix[k + 1] - prefix[l]
                right = prefix[r + 1] - prefix[k + 1]

                if left < right:
                    ans = max(ans, left + dfs(l, k))
                elif left > right:
                    ans = max(ans, right + dfs(k + 1, r))
                else:
                    ans = max(
                        ans,
                        left + max(dfs(l, k), dfs(k + 1, r))
                    )
            return ans

        return dfs(0, n - 1)

ans = Solution().stoneGameV([6,2,3,4,5,5])
print(ans)