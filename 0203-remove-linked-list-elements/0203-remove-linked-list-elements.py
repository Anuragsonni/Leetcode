# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        if head.val == val:
            head = head.next
            head = self.removeElements(head, val)

        tail = head 
        pre = tail
        while tail :
            pre = tail
            tail = tail.next 
            if tail and tail.val == val:
                break
        

        if tail:
            pre.next = tail.next
            head = self.removeElements(head, val)
        
        return head


