# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head.next
        slow=head
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        
        tail1 = slow 
        slow = slow.next 
        tail1 = None 

        curr = slow
        pre = None
        while curr :
            nxt = curr.next
            curr.next = pre 
            pre = curr
            curr = nxt
        
        tail = head
        while pre and tail:
            if pre.val != tail.val:
                return False
            pre = pre.next
            tail = tail.next
        return True