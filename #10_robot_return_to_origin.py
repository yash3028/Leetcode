class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u,d,l,r = 0,0,0,0
        for i in moves:
            if i=="U":
                u+1
            if i=="D":
                d+=1
            if i=="L":
                l+=1
            if i=="R":
                r+=1
        if u-d==0 and l-r==0:
            return True
        else:
            return False
ans = Solution().judgeCircle("UD")
print(ans)