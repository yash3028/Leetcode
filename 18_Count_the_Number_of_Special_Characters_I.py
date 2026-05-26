class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # convert string to set 
        st = set(word)

        count = 0
        # iterate through all letters
        for i in range(26):
            # lowercase for every letter
            lower = chr(ord('a') + i)
            # uppercase
            upper = chr(ord('A') + i)
            # if both exist in set then increament count
            if lower in st and upper in st:
                count += 1

        return count
    
ans = Solution().numberOfSpecialChars("aaAbcBC")
print(ans)