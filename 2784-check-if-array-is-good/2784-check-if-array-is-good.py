from collections import Counter
class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        return nums== list(range(1,len(nums)))+ [len(nums)-1]