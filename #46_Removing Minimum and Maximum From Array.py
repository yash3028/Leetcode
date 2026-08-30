from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        m = n // 2

        # [value, index]
        lmin = [float('inf'), -1]
        lmax = [float('-inf'), -1]
        rmin = [float('inf'), -1]
        rmax = [float('-inf'), -1]
        #left part of nums to find min and max
        for i in range(m):
            if nums[i] < lmin[0]:
                lmin = [nums[i], i]
            if nums[i] > lmax[0]:
                lmax = [nums[i], i]
        #right part of array to find min and max
        for i in range(m, n):
            if nums[i] < rmin[0]:
                rmin = [nums[i], i]
            if nums[i] > rmax[0]:
                rmax = [nums[i], i]
        #comparing left and right min and max
        mn = lmin if lmin[0] < rmin[0] else rmin
        mx = lmax if lmax[0] > rmax[0] else rmax

        left = min(mn[1], mx[1])
        right = max(mn[1], mx[1])
        # checking from where we can get minimum deletions
        return min(
            right + 1,
            n - left,
            left + 1 + n - right
        )

ans = Solution().minimumDeletions([2,10,7,5,4,1,8,6])
print(ans)