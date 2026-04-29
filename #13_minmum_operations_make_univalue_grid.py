from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        #convert 2d to 1d array
        one_d = [item for row in grid for item in row]
        rem = one_d[0]%x
        #check if all elements are different then reutrn -1
        for i in one_d:
            if i%x!=rem:
                return -1
        one_d.sort()
        #we will select median value to convert all other elements to its value
        #why median if two elements on opposite direction of each other the minimum common
        #point for two of them is median
        median = one_d[len(one_d)//2]
        cnt = 0
        for num in one_d:
           #formula to find number of times a number needed to add or subtract from a number
           cnt+=abs(num-median)/x
        return int(cnt)

ans = Solution().minOperations([[2,4],[6,8]],2)
print(ans)