class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            #shift ans by one left bit to make space for new bit
            ans = ans<<1
            #last bit of n and adding it to ans by or operater
            ans = ans | (n&1)
            #right shift by 1 for next bit to iterate
            n = n >> 1
        return ans
    
ans = Solution().reverseBits(43261596)
print(ans)