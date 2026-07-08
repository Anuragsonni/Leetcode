class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=len(nums)
        if max(nums)!= l-1:
            return False
        for i in range(1,l):
            if i in nums:
                pass 
            else:
                return False
        nums.remove(l-1)
        if l-1 in nums:
            return True
        else :
            return False