class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n + 11):
            prod = 1
            x = i

            while x > 0:
                prod *= x % 10
                x //= 10

            if prod % t == 0:
                return i

ans = Solution().smallestNumber(10,2)
print(ans)