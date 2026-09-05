class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # prefic maximum array
        maxi = [0] * n
        # suffix minimum array
        mini = [0] * n

        maxi[0] = nums[0]
        # build prefix maximum array from num[0] to nums[i]
        for i in range(1, n):
            maxi[i] = max(maxi[i - 1], nums[i])

        mini[n - 1] = nums[n - 1]
        # build suffic minimum array from nums[i] to nums[n-1]
        for i in range(n - 2, -1, -1):
            mini[i] = min(mini[i + 1], nums[i])

        # find stable element
        for i in range(n):
            if maxi[i] - mini[i] <= k:
                return i

        return -1

ans = Solution().firstStableIndex([5,0,1,4],3)
print(ans)