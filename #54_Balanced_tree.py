class Solution:
    def isBalanced(self, root):
        return self.height(root) != -1

    def height(self, node):
        if node is None:
            return 0

        left = self.height(node.left)
        if left == -1:
            return -1

        right = self.height(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1

