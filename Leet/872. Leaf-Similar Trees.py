# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:


        def add_l(root: TreeNode, list):
            if root.left:
                add_l(root.left, list)
            elif not root.left and not root.right:
                list.append(root.val)
            if root.right:
                add_l(root.right, list)
            return list

        list1 = []
        list2 = []

        if add_l(root1, list1) == add_l(root2, list2):
            return True
        return False

if __name__ == "__main__":
    senate = list(input().split(','))
    l1 = TreeNode(senate[0])
    l2 = TreeNode(senate[1])
    l3 = TreeNode(senate[2])
    l1.left = l2
    l1.right = l3
    l4 = TreeNode(senate[3])
    l5 = TreeNode(senate[4])
    l2.left = l4
    l2.right = l5
    l6 = TreeNode(senate[5])
    l7 = TreeNode(senate[6])
    l3.left = l6
    l3.right = l7
    l8 = TreeNode(senate[9])
    l9 = TreeNode(senate[10])
    l5.left = l8
    l5.right = l9

    print([1, 2, 3] == [1,3,2])

    s = Solution()
    #print(s.leafSimilar(l1, l2))