from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            even = set()
            odd = set()
            #searching every sub array
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])

                #balance distinct odd and even should be equal 
                if len(even) == len(odd):
                    #maximum length until current iteration
                    ans = max(ans, j - i + 1)

        return ans

ans = Solution().longestBalanced([2,5,4,3])
print(ans)
