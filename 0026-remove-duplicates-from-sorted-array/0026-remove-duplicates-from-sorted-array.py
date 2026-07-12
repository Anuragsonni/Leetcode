class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 1
        for r in range(len (nums)-1):
            if nums[r]!=nums[r+1]:
                nums[w] = nums[r+1]
                w+=1
        return w