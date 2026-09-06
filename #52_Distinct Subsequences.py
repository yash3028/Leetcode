class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        # If s is shorter than t is impossible
        if m < n:
            return 0

        # dp array store the answer 
        dp = []
        for i in range(m + 1):
            row = []
            for j in range(n + 1):
                row.append(-1)
            dp.append(row)

        def solve(m, n):
            if n == 0:
                return 1
            if m == 0:
                return 0

            # return the stored answer if already computed
            if dp[m][n] != -1:
                return dp[m][n]

            # If current characters match:
            if s[m - 1] == t[n - 1]:
                # include char and exlucde current char
                dp[m][n] = solve(m - 1, n) + solve(m - 1, n - 1)
            else:
                # char does not match so skip current char of s
                dp[m][n] = solve(m - 1, n)

            return dp[m][n]

        return solve(m, n)