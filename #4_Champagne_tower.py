class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        #liquid passing through first glass flow
        prev = [poured]
        for row in range(1,query_row+1):
            #every row has +1 than prev row
            curr = [0]*(row+1)
            for i in range(row):
                #-1 as that glass is filled with liquid 
                extra = prev[i]-1
                if extra>0:
                    #0.5 as it divides with two glasses it get 50% of parent liquid
                    curr[i] += 0.5*extra
                    curr[i+1] += 0.5*extra
            prev = curr
        return min(1,prev[query_glass])
    

ans = Solution().champagneTower(2,1,1)
print(ans)