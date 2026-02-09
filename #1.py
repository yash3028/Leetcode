#Balances Binary Search Tree
from collections import deque
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Inorder to sort the tree
        def inorder(node,res):
            if node is None:
                return
            inorder(node.left,res)
            res.append(node.val)
            inorder(node.right,res)
        res = []
        inorder(root,res)
        #construct a balanced bst from sorted values
        def contruct(tree):
            if not tree:
                return
            #Choosing middle element to keep tree balance
            m = len(tree)//2
            node = TreeNode(tree[m])
            node.left = contruct(tree[:m])
            node.right = contruct(tree[m+1:])
            return node
        return contruct(res)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

ans = Solution().balanceBST(root)

def print_tree(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            print(node.val, end=" ")
            q.append(node.left)
            q.append(node.right)
print_tree(ans)