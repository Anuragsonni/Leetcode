from collections import Counter
class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nums.sort()
        # return nums== list(range(1,len(nums)))+ [len(nums)-1]
        l = len(nums)

        if max(nums) != l - 1:
            return False

        for i in range(1, l):
            if i not in nums:
                return False

        nums.remove(l - 1)

        return (l - 1) in nums