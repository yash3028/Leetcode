from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)
        num = k
        #iterate through nums
        for i in range(n):
            #if k not in nums return k
            if num not in nums:
                return num
            #next multiple of k
            num = num+k
        return num
ans = Solution().missingMultiple([99],99)
print(ans)