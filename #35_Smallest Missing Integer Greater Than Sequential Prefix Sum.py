from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        n = len(nums)
        for i in range(1,n):
            if nums[i] == nums[i - 1] + 1:
                total+=nums[i]
            else: 
                break
        
        while total in nums:
            total+=1
        return total
ans = Solution().missingInteger([1,2,3,2,5])
print(ans)