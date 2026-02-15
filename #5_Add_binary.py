class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        carry = 0
        n1 = len(a)
        n2 = len(b)
        #in string left to right easy to calculate but bit addition is from right to left so we reverse
        a,b = a[::-1],b[::-1]
        for i in range(max(n1,n2)):
            #if no digit at that place take 0
            numA = ord(a[i])-ord("0") if i<n1 else 0
            numB = ord(b[i]) - ord("0") if i<n2 else 0
            total = numA + numB + carry
            #%2 because binary base
            digit = str(total%2)
            ans = digit + ans
            carry = total//2

        if carry:
            ans = "1"+ans

        return ans
    
ans = Solution().addBinary("11","1")
print(ans)