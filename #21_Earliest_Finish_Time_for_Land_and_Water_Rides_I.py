from typing import List
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')
        # we will find the time to complete both ride starting with land ride
        for i in range(len(landStartTime)):

            landEnd = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):

                waterBegin = max(landEnd, waterStartTime[j])

                finish = waterBegin + waterDuration[j]

                ans = min(ans, finish)
        # time to complete both rides starting with water ride
        for i in range(len(waterStartTime)):

            waterEnd = waterStartTime[i] + waterDuration[i]

            for j in range(len(landStartTime)):

                landBegin = max(waterEnd, landStartTime[j])

                finish = landBegin + landDuration[j]

                ans = min(ans, finish)

        return ans
ans = Solution().earliestFinishTime([2,8],[4,1],[6],[3])
print(ans)