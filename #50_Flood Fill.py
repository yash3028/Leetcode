class Solution:
    def floodFill(self, image, sr, sc, color):
        # first color 
        old = image[sr][sc]
        # if old color is equal to new then return image
        if old == color:
            return image

        rows, cols = len(image), len(image[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if image[r][c] != old:
                return
            # changing old color to new color
            image[r][c] = color

            # search until last row
            dfs(r + 1, c)
            # search until stat row of image
            dfs(r - 1, c)
            # search until last column of image
            dfs(r, c + 1)
            # search until first column of image
            dfs(r, c - 1)

        dfs(sr, sc)
        return image

ans = Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2)
print(ans)