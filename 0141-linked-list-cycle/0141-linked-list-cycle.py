# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not (head and head.next) :
            return False

        slow = fast = head 
        fast = fast.next

        while slow != fast:
            if not (fast and fast.next):
                return False 
            
            slow = slow.next
            fast = fast.next.next
        
        return True

        # seen = set()
        # while tail :
        #     if tail.next in seen and tail.next is not None:
        #         return True
        #     seen.add(tail.next)
        #     tail = tail.next
        
        # return False

        # seen = set()
        # tail = head 

        # while tail not in seen :
        #     seen.add(tail.next)
        #     tail = tail.next
        #     if tail is None:
        #         return False
        
        # return True