# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return head
        temp_head = ListNode()
        r_head= temp_head
        

        while temp_head:
            tail = head
            afterTail = head.next
            if afterTail != None :
                while afterTail.next:
                    afterTail = afterTail.next
                    tail = tail.next

                temp_head.next = afterTail
                temp_head = temp_head.next
                tail.next = None
            else:
                temp_head.next = tail
                temp_head = temp_head.next
                temp_head = None

        return r_head.next          