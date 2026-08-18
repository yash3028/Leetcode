from typing import Counter, List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        #count repeating numbers
        freq = Counter(nums)
        cnt=[]
        #if size of subarray is 1 then we can return max element which has appeared once
        if k==1:
            for i in freq:
                if freq[i]==1:
                    cnt.append(i)
            if cnt:
                return max(cnt)
            else:
                return -1
        # if k is length of array then we can print max from array
        if k==n:
            return max(nums)

        ans = []
        #size of sub array is greater than one then all elements will appear twice in a subarray
        # so we find first and last ele of array and return max of those two
        if freq[nums[0]]==1:
            ans.append(nums[0])
        if freq[nums[-1]]==1:
            ans.append(nums[-1])

        if ans: 
            return max(ans)
        else:
            return -1
            
ans = Solution().largestInteger([3,9,2,1,7],3)
print(ans)