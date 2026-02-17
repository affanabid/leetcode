# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        odd, even, temp = head, head.next, head.next
        while True:
            if not odd.next or not even.next:
                odd.next = temp
                break
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        return head
            