# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        dummy = ListNode()
        dummy.next = head
        pre = dummy 
        slow = head
        fast = head.next 
        while True :
            pre.next = fast
            slow.next = fast.next
            fast.next = slow 
            # update pointer
            pre = pre.next.next
            slow = slow.next
            if fast.next.next and fast.next.next.next:
                fast = fast.next.next.next
            else :
                break
        return dummy.next