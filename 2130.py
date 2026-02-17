from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        f, s, mx, st = head, head, 0, []
        while s:
            st.append(f.val)
            f = f.next
            s = s.next.next
        while st:
            mx = max(mx, st.pop() + f.val)
            f = f.next
        return mx
        

a = ListNode(5)
a.next = ListNode(4)
a.next.next = ListNode(2)
a.next.next.next = ListNode(1)

s = Solution()
print(s.pairSum(a))
# c = a
# while c:
#     print(c.val, end=' ')
#     c = c.next