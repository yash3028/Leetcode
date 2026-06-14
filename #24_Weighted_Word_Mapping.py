from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        #iterate through our words array
        for word in words:
            total = 0
            #iterate through every char in that word
            for ch in word:
                total += weights[ord(ch) - ord('a')]

            rem = total % 26
            #we will subtract from z to find reverse order
            ans.append(chr(ord('z') - rem))

        return "".join(ans)
    
ans = Solution().mapWordWeights(["abcd","def","xyz"],[5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2])
print(ans)