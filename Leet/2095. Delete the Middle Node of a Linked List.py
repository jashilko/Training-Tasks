# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        slow, fast, prev = head, head, head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head


if __name__ == "__main__":

    senate = list(input().split(','))
    head = None
    for i in reversed(range(len(senate))):
        head = ListNode(senate[i], head)
    s = Solution()
    print(s.deleteMiddle(head))