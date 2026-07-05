class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # w,r=0,0
        # for r in range(len(nums)-1):
        #     if nums[r] == nums[r+1]:
        #         pass
        #     else:
        #         w+=1
        #         nums [ w ] = nums [ r+1 ]

        # return w+1
        if not nums:
            return 0

        w = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[w] = nums[r]
                w += 1

        return w