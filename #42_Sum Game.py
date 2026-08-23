class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        #split nums into two arrays
        left = num[:n // 2]
        right = num[n // 2:]
        s1 = s2 = 0
        q1 = q2 = 0
        #find how many ? on left array and sum of left array
        for ch in left:
            if ch == '?':
                q1 += 1
            else:
                s1 += int(ch)
        #find many ? on right array and sum of right array
        for ch in right:
            if ch == '?':
                q2 += 1
            else:
                s2 += int(ch)
        total = q1+q2
        #if sum of ? on left and right are odd then alice will win because she has last chance to 
        #replace
        if total % 2==1:
            return True
        l = 2*s1 + 9*q1
        r = 2*s2 + 9*q2

        return l!=r
ans = Solution().sumGame("5023")
print(ans)