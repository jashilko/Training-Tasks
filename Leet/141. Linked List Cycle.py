
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True


        return False

if __name__ == "__main__":

    senate = list(input().split(','))
    pos = int(input())
    head = None
    j = 0
    for i in reversed(range(len(senate))):
        head = ListNode(senate[i], head)
        if i == len(senate) - 1:
            last = head
        if pos > 0 and pos == len(senate) - i - 1:
            last.next = head
        j += 1

    s = Solution()
    new_head = s.hasCycle(head)

    # while new_head:
    #     print(new_head.val)
    #     new_head = new_head.next
    #print(s.oddEvenList(head))