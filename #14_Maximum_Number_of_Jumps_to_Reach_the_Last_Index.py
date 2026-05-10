from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        arr = [-1]*n
        arr[0]=0
        for i in range(1,n):
            for j in range(i):
                if abs(nums[i]-nums[j])<=target and arr[j]!=-1:
                # there can be multiple ways to reach index we need maximum number of jumps 
                    arr[i]=max(arr[i],arr[j]+1)

        return arr[-1]
ans = Solution().maximumJumps([1,3,6,4,1,2],2)
print(ans)