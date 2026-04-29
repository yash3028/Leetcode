from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        one_d = [item for row in grid for item in row]
        rem = one_d[0]%x
        for i in one_d:
            if i%x!=rem:
                return -1
        one_d.sort()
        median = one_d[len(one_d)//2]
        cnt = 0
        for num in one_d:
           cnt+=abs(num-median)/x
        return int(cnt)

ans = Solution().minOperations([[2,4],[6,8]],2)
print(ans)