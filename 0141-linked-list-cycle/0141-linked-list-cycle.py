# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tail = head 
        seen = set()
        while tail:
            if tail in seen:
                return True
            seen.add(tail)
            tail = tail.next
        
        return False