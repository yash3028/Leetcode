# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        prev = head
        temp = head.next

        # store index of first and last critical points
        first = -1
        last = -1

        # current index of temp 
        idx = 0

        # minimum distance between critical points
        mini = float('inf')

        # traverse while current node has a next node
        while temp.next:
            idx += 1

            # check if current node is a local maxima or minima
            if (prev.val < temp.val and temp.val > temp.next.val) or \
               (prev.val > temp.val and temp.val < temp.next.val):

                # update minimum distance from previous critical point
                if last != -1:
                    mini = min(mini, idx - last)

                # update last critical point index
                last = idx

                # reecord first critical point only once
                if first == -1:
                    first = idx

            prev = temp
            temp = temp.next
        if first == last:
            return [-1, -1]
        return [mini, last - first]

ans = Solution().nodesBetweenCriticalPoints([3,1])
print(ans)