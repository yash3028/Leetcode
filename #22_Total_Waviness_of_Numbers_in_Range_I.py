class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # count waviness
        ans = 0
        # iterate through every number
        for x in range(num1, num2 + 1):
            # Convert number to string 
            s = str(x)
            # Check every middle digit
            for i in range(1, len(s) - 1):
                # current digit is greater than both neighbors
                # current digit is smaller than both neighbors
                if ((s[i] > s[i - 1] and s[i] > s[i + 1]) or
                    (s[i] < s[i - 1] and s[i] < s[i + 1])):
                    ans += 1
        return ans
    
ans = Solution().totalWaviness(120,130)
print(ans)