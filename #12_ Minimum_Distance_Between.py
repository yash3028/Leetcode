from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mp = {}
        for i, num in enumerate(nums):
            if num not in mp:
                mp[num] = []
            mp[num].append(i)
        ans = float('inf')
        print(mp)
        for key,values in mp.items():
            if len(values)>=3:
                for i in range(len(values)-2):
                    maxi = values[i+2]
                    mini = values[i]
                    ans = min(ans,2*(maxi-mini))

        if ans == float('inf'):
            return -1
        else:
            return ans

ans = Solution().minimumDistance([1,2,1,1,3])
print(ans)