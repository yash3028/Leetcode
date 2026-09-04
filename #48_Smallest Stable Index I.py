class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            # maximum ele till ith index
            maxi = float('-inf')
            # minimum ele from i+1 to end of nums
            mini = float('inf')

            for j in range(i + 1):
                maxi = max(maxi, nums[j])

            for j in range(i, n):
                mini = min(mini, nums[j])
            # smallest stable index
            if maxi - mini <= k:
                return i
        return -1

ans = Solution().firstStableIndex([5,0,1,4],3)
print(ans)