from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        # Total sum of elements
        right = sum(nums)
        left = 0
        ans = [0] * len(nums)
        # iterate through array
        for i in range(len(nums)):
            
            # Remove current element from right sum
            # so that current elements containts sum of all elements to its right
            right -= nums[i]

            #difference between left  and right sum
            ans[i] = abs(left - right)

            # Add current element to left sum
            left += nums[i]

        return ans