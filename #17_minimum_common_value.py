from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2= len(nums1), len(nums2)
        num1, num2=0, 0
        while num1<n1 and num2<n2:
            x=nums1[num1]
            y=nums2[num2]
            #if first index is equal in both arr then return that as it is minimum
            if x==y: 
                return x
            #if ele in arr1 is greater than arr2 than increment num2 counter
            elif x>y: 
                num2+=1
            #if ele in arr2 is greater than arr1 increment num1 counter
            else: num1+=1
        return -1
    
ans = Solution().getCommon([1,2,3],[2,4])
print(ans)
        