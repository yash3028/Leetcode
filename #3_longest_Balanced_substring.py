class Solution:
    def longestBalanced(self, s: str) -> int:
        #to find length of string
        ans = 0
        n = len(s)
        for i in range(n):
            #to store character frequency
            freq = [0]*26
            #how many different character are used
            diff = 0
            #frequency of a single character
            max_f = 0
            for j in range(i,n):
                idx = ord(s[j]) - ord('a')
                if freq[idx]==0:
                    diff+=1
                freq[idx]+=1
                max_f = max(max_f,freq[idx])
                length = j - i + 1
                #if length of substring balances (diff=2,max_f=2 then length should be 4)condition for balanced substring
                if length == diff*max_f:
                    ans = max(ans,length)

        return ans

ans = Solution().longestBalanced("abbac")
print(ans)