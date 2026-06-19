class Solution:
    def largestAltitude(self, gain):
        n = len(gain)
        mx = 0
        # iterate through all positions n+1 because of starting position
        for i in range(n + 1):
            alt = 0
            #find altitude at index i
            for j in range(i):
                alt += gain[j]
            #update the max altitude
            mx = max(mx, alt)

        return mx
ans = Solution().largestAltitude([-5,1,5,0,-7])
print(ans)