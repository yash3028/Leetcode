class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n=len(s)
        ans = ""
        for i in range(n):
            cnt = 0
            res = ""
            for j in range(i,n):
                res+=s[j]
                if s[j]=='1':
                    cnt+=1
                if cnt>k:
                    break
                if cnt == k:
                    if ans == "" or len(res) < len(ans) or (len(res) == len  (ans) and res < ans):
                        ans = res
        return ans
ans = Solution().shortestBeautifulSubstring("100011001",3)
print(ans)