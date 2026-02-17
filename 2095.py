from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import math
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getLength(curr):
            count = 0
            while curr:
                count += 1
                curr = curr.next
            return count
        length = getLength(head)
        i = math.floor(length / 2)
        c = 0
        curr = head
        if length == 1:
            return
        while curr:
            if c+1 == i:
                curr.next = curr.next.next
            c += 1
            curr = curr.next
        return head


        