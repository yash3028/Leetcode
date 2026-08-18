from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        # prefix sum to calculate sum of sub array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
        # iterate every stone
        def dfs(l: int, r: int) -> int:
            #if onle one stone is left
            if l == r:
                return 0

            ans = 0
            # every possible split
            for k in range(l, r):
                #sum of left split
                left = prefix[k + 1] - prefix[l]
                #sum of right split
                right = prefix[r + 1] - prefix[k + 1]
                #if left has smaller sum add it to alice 
                if left < right:
                    ans = max(ans, left + dfs(l, k))
                # if right is smaller add right
                elif left > right:
                    ans = max(ans, right + dfs(k + 1, r))
                # if left and right are equal add any one side
                else:
                    ans = max(
                        ans,
                        left + max(dfs(l, k), dfs(k + 1, r))
                    )
            return ans

        return dfs(0, n - 1)

ans = Solution().stoneGameV([6,2,3,4,5,5])
print(ans)



# class Solution {
#     int[][] t = new int[501][501];

#     public int solve(int l, int r, int[] cumSum) {
#         if(l >= r) {
#             return 0; 
#         }
#         if(t[l][r] != -1) {
#             return t[l][r];
#         }
#         int score = 0;
#         for(int mid = l; mid <= r-1; mid++) {
#             int leftSum  = cumSum[mid] - (l-1 >= 0 ? cumSum[l-1] : 0);
#             int rightSum = cumSum[r] - cumSum[mid]; 
#             if(leftSum < rightSum) {
#                 score = Math.max(score, leftSum + solve(l, mid, cumSum));
#             } else if(leftSum > rightSum) {
#                 score = Math.max(score, rightSum + solve(mid+1, r, cumSum));
#             } else {
#                 score = Math.max(score, Math.max(leftSum + solve(l, mid, cumSum), rightSum + solve(mid+1, r, cumSum)));
#             }
#         }
#         return t[l][r] = score;
#     }

#     public int stoneGameV(int[] stoneValue) {
#         int n = stoneValue.length;
#         int[] cumSum = new int[n];
#         cumSum[0] = stoneValue[0];
#         for(int i = 1; i < n; i++) {
#             cumSum[i] = cumSum[i-1] + stoneValue[i];
#         }
#         for(int[] row : t) {
#             Arrays.fill(row, -1);
#         }
#         return solve(0, n-1, cumSum);
#     }
# }
