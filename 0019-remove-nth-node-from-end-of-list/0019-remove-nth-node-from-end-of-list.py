# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        if not n:
            return head
        
        dummy = ListNode()
        dummy.next = head
        nodes=0
        tail = dummy
        while tail.next:
            tail= tail.next
            nodes += 1 
        
        delete = nodes - n 
        tail = dummy
        
        while delete>0:
            tail = tail.next
            delete -= 1
        tail.next = tail.next.next

        return dummy.next