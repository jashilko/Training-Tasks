# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        odd = head
        evenHead = even = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = evenHead
        return head

if __name__ == "__main__":

    senate = list(input().split(','))
    head = None
    for i in reversed(range(len(senate))):
        head = ListNode(senate[i], head)
    s = Solution()
    new_head = s.oddEvenList(head)

    while new_head:
        print(new_head.val)
        new_head = new_head.next
    #print(s.oddEvenList(head))