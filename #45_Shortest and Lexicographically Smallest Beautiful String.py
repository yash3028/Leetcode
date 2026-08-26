class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n=len(s)
        #to store the shortest substring
        ans = ""
        #iterate through the string
        for i in range(n):
            #count the ones
            cnt = 0
            #to store the beautiful substring
            res = ""
            #iterate through string from current index
            for j in range(i,n):
                res+=s[j]
                #is string at indes is 1 increament cnt
                if s[j]=='1':
                    cnt+=1
                #if cnt greater than k then break we cant find beautiful string
                if cnt>k:
                    break
                #cnt ==k then we compare with previous substring stored in res
                if cnt == k:
                    if ans == "" or len(res) < len(ans) or (len(res) == len  (ans) and res < ans):
                        ans = res
        return ans
ans = Solution().shortestBeautifulSubstring("100011001",3)
print(ans)