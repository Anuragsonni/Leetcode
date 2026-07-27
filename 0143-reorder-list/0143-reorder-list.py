# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        lis = []
        tail= head
        while tail:
            lis.append(tail.val)
            tail = tail.next
        
        l= len(lis)
        ans=[]
        if l%2:
            rev = lis[l//2 +1 : ]
        else:
            rev = lis[l//2 : ]
        
        rev.reverse()
        i = j = 0

        for k in range (l):
            if k%2 :
                ans.append(rev[j])
                j+=1

            else:
                ans.append(lis[i])
                i+=1
        
        tail= head
        for i in ans:
            tail.val = i
            tail= tail.next