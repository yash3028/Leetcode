from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        # iterate through the array
        for l in range(n):
            cnt = 0
            # subarray for every index
            for r in range(l, n):
                # if element is equal target increament cnt
                if nums[r] == target:
                    cnt += 1
                # length of our subarray
                length = r - l + 1
                # if length of subarray is greater than half of array then we found a subarray with majority element
                if cnt > length // 2:
                    ans += 1

        return ans

ans = Solution().countMajoritySubarrays([1,2,2,3],2)
print(ans)