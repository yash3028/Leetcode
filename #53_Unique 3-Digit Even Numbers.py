class Solution:
    def totalNumbers(self, digits):
        n = len(digits)
        seen = set()  
        for h in range(n):
            #  3 digit number cannot start with 0
            if digits[h] == 0:
                continue

            # choose the tenth place digit
            for t in range(n):
                # we will skip if same number is reused
                if t == h:
                    continue

                # selecting ones place digit
                for u in range(n):
                    #  three indices must be different
                    if u == h or u == t:
                        continue

                    # number must be even so last digit must be even
                    if digits[u] % 2 != 0:
                        continue

                    # add the 3 didgit number
                    num = digits[h] * 100 + digits[t] * 10 + digits[u]
                    seen.add(num)
        return len(seen)
ans = Solution().totalNumbers([1,2,3,4])
print(ans)