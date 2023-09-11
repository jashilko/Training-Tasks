# Definition for a binary tree node.
from sys import maxsize


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def count_good(root: TreeNode, max_val, cnt_good):
            # Прямой проход
            if root:
                max_val = max(root.val, max_val)
                if root.val >= max_val:
                    cnt_good += 1

                if root.left:
                    cnt_good = count_good(root.left, max_val, cnt_good)
                if root.right:
                    cnt_good = count_good(root.right, max_val, cnt_good)

                return cnt_good

        return count_good(root, -maxsize-1, 0)

if __name__ == "__main__":
    senate = list(map(int, input().split(',')))
    l1 = TreeNode(senate[0])
    l2 = TreeNode(senate[1])
    l3 = TreeNode(senate[2])
    l1.left = l2
    l1.right = l3
    l4 = TreeNode(senate[3])
    #l5 = TreeNode(senate[4])
    l2.left = l4
    #l2.right = l5
    l6 = TreeNode(senate[5])
    l7 = TreeNode(senate[6])
    l3.left = l6
    l3.right = l7
    #l8 = TreeNode(senate[9])
    #l9 = TreeNode(senate[10])
    #l5.left = l8
    #l5.right = l9

   #print([1, 2, 3] == [1,3,2])

    s = Solution()
    print(s.goodNodes(l1))
