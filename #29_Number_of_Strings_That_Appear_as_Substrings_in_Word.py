from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt = 0
        for i in patterns:
            if i in word:
                cnt+=1
        return cnt
ans = Solution().numOfStrings( ["a","abc","bc","d"],["abc"])
print(ans)