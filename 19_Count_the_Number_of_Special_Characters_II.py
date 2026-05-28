class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Stores the last position of each lowercase character
        last_lower = {}
        # Stores the first position of each uppercase character
        first_upper = {}
        # iterate the string with index
        for i, ch in enumerate(word):
            # If char is lowercase
            if ch.islower():
                # we will Update its latest occurrence
                last_lower[ch] = i
            else:
                lower = ch.lower()
                # Store only the first uppercase occurrence
                if lower not in first_upper:
                    first_upper[lower] = i
        count = 0
        # Check every lowercase character found
        for ch in last_lower:
            # uppercase exists and last lowercase index comes before first uppercase index
            if ch in first_upper and last_lower[ch] < first_upper[ch]:
                count += 1

        return count
    
ans = Solution().numberOfSpecialChars("aaAbcBC")
print(ans)