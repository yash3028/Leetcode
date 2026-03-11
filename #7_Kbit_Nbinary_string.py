class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        cnt = 0
        while n>1:
            length = 2 ** n - 1
            m = length//2+1
            if k==m:
                # we are starting with original value k
                if cnt%2==0:
                    return "1"
                else:
                    return "0"
            # if k is on right of mid then we have to invert the right side instead we using left part
            # as it is inverse of right side 
            if k>m:
                k = length - k + 1
                cnt+=1
            n-=1
        # we arrive at base case s1=0
        if cnt%2==0:
            return "0"
        else:
            return "1"
        
ans = Solution().findKthBit(4,11)
print(ans)