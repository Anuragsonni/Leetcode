class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        win = 1
        maxl = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                win+=1
            else:
                win=1
            maxl=max(win, maxl)
        
        return maxl