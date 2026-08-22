class Solution:
    def checkDivisibility(self, n: int) -> bool:
        new = n
        add = 0
        mul = 1
        #dividing n by 10 
        while n>0:
            num=n%10
            #adding rem
            add+=num
            #multiplying rem
            mul*=num
            n=n//10
        #sum of rem and mul
        total = add+mul
        print(total)

        if new%total==0:
            return True
        else:
            return False

ans = Solution().checkDivisibility(99)
print(ans)