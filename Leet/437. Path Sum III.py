# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    cnt = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, start, s):
            if not root:
                return
            s -= root.val
            if s == 0:
                self.cnt += 1
            dfs(root.left, False, s)
            dfs(root.right, False, s)
            if start:
                dfs(root.left, True, targetSum)
                dfs(root.right, True, targetSum)

        dfs(root, True, targetSum)
        return self.cnt

if __name__ == "__main__":
    senate = list(input().split(','))
    l1 = TreeNode(int(senate[0]))
    l2 = TreeNode(int(senate[1]))
    l3 = TreeNode(int(senate[2]))
    l1.left = l2
    l1.right = l3
    l4 = TreeNode(int(senate[3]))
    l5 = TreeNode(int(senate[4]))
    l2.left = l4
    l2.right = l5
    #l6 = TreeNode(senate[5])
    l7 = TreeNode(int(senate[6]))
    #l3.left = l6
    l3.right = l7
    l8 = TreeNode(int(senate[7]))
    l9 = TreeNode(int(senate[8]))
    l4.left = l8
    l4.right = l9
    #l10 = TreeNode(senate[9])
    l11 = TreeNode(int(senate[10]))
    l5.right = l11

   #print([1, 2, 3] == [1,3,2])
    targetSum = int(input())
    s = Solution()
    print(s.pathSum(l1, targetSum))