from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Добавляем к дереву элемент
def add(tn: TreeNode, newVal: int):
    key = tn.val
    if newVal < key: # идём влево
        if not tn.left:
            tn.left = TreeNode(newVal)
        else:
            add(tn.left, newVal)
    elif newVal > key:
        if not tn.right:
            tn.right = TreeNode(newVal)
        else:
            add(tn.right, newVal)


class Solution:

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)


if __name__ == "__main__":
    nums = list(map(int, input().split(',')))
    val = int(input())
    for i in range(len(nums)):
        if i == 0:
            tn_init = TreeNode(nums[i])
        else:
            add(tn_init, nums[i])
    s = Solution()
    s.searchBST(tn_init, val)
