# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not (head and head.next):
            return
        
        fast = head.next
        slow = head

        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None

        curr = second
        pre = None
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt

        count = 1 
        tail = head 
        
        while tail and pre :
            mid = pre
            pre = pre.next 
            mid.next = tail.next
            tail.next = mid 
            tail = tail.next.next