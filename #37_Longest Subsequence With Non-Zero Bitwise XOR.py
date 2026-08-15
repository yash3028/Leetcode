from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = nums[0]
        n = len(nums)
        for i in range(1,n):
            total^=nums[i]
        if total!=0:
            return n
    
        if all(num == 0 for num in nums):
            return 0
        return n-1

ans = Solution().longestSubsequence([1,2,3])
print(ans)