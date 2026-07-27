# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        seen = set()
        dummy = ListNode()
        dummy.next = head
        tail = dummy 
        while tail.next:
            if tail.next.val in seen :
                tail.next = tail.next.next
            else:
                seen.add(tail.next.val)
                tail = tail.next
            
        return head