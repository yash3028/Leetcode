from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cnt = 0
        rows = len(mat)
        cols = len(mat[0])
        # r and c used to track all 1 places in matrix
        r = [0]*rows
        c = [0]*cols
        # find all place where row and col are set to 1
        for row in range(rows):
            for col in range(cols):
                if mat[row][col]==1:
                    r[row]+=1
                    c[col]+=1
        # if the place is special and the row or col are visited once then increment
        for row in range(rows):
            for col in range(cols):
                if mat[row][col]==1 and r[row]==1 and c[col]==1:
                    cnt+=1
        return cnt

ans = Solution().numSpecial([[1,0,0],[0,0,1],[1,0,0]])
print(ans)