# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        dummy = ListNode()
        dummy.next = node
        tail = dummy
        while tail.next.next :
            tail.val = tail.next.val
            tail = tail.next 
        tail.val = tail.next.val
        tail.next = None
        
        # dummy = ListNode(0)
        # dummy.next = head
        # tail = dummy
        # while tail.next:
        #     if tail.next == node:
        #         tail.next = tail.next.next
        #     else :
        #         tail= tail.next