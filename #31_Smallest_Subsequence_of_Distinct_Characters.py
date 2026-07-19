class Solution:
    def smallestSubsequence(self, s: str) -> str:
        mp = {}
        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1

        st = []
        # keep track of character already present in st
        seen = set()

        # iterate through each char
        for ch in s:
            # decrease the count of current char
            mp[ch] -= 1 

            # if char is already used continue 
            if ch in seen:
                continue
            # remove char if our top char appear again and current char is lexicographically smaller
            while st and ch < st[-1] and mp[st[-1]] > 0:
                seen.remove(st.pop())

            st.append(ch)
            seen.add(ch)

        return "".join(st)
    
ans = Solution().smallestSubsequence("bcabc")
print(ans)