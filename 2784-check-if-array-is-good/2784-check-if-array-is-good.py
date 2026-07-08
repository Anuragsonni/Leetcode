from collections import Counter
class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)-1
        
        count = Counter(nums)
        if count[n] !=2:
            return False
        for i in range(1,n):
            if count[i] != 1:
                return False 
        return True