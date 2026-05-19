from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        #if arr has one element then we reached last index 
        if n == 1:
            return 0
        #Store all indices for each value
        graph = defaultdict(list)

        for i, val in enumerate(arr):
            graph[val].append(i)

        #to store index and number of steps
        q = deque([(0, 0)])  
        visited = set([0])

        while q:
            i, steps = q.popleft()
            #if we reach end of arr then we return steps
            if i == n - 1:
                return steps

            neighbors = []
            #adjacent neibhours left and right of current index
            neighbors.append(i + 1)
            neighbors.append(i - 1)

            neighbors.extend(graph[arr[i]])
            #visit all possible positions
            for nei in neighbors:
                if 0 <= nei < n and nei not in visited:
                    visited.add(nei)
                    q.append((nei, steps + 1))

            graph[arr[i]].clear()

        return -1
    
ans = Solution().minJumps([100,-23,-23,404,100,23,23,23,3,404])
print(ans)