# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
if __name__ == "__main__":

    senate = list(input().split(','))
    head = None
    for i in reversed(range(len(senate))):
        head = ListNode(senate[i], head)
    s = Solution()
    new_head = s.reverseList(head)

    while new_head:
        print(new_head.val)
        new_head = new_head.next
    #print(s.oddEvenList(head))