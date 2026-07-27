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
        dummy = ListNode()
        dummy.next = head
        tail = dummy 
        while tail.next and tail.next.next:
            if tail.next.val == tail.next.next.val:
                tail.next = tail.next.next
            else:
                tail = tail.next
            
        return dummy.next
        # seen = set()
        # dummy = ListNode()
        # dummy.next = head
        # tail = dummy 
        # while tail.next:
        #     if tail.next.val in seen :
        #         tail.next = tail.next.next
        #     else:
        #         seen.add(tail.next.val)
        #         tail = tail.next
            
        # return head