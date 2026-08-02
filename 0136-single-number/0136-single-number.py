# from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums :
            if nums.count(i)==1:
                return i
        
        # count= Counter(nums)
        # for i in count:
        #     if count[i] == 1 :
        #         return i 