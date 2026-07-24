class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        smallest = 5000 
        while l<=r :
            mid = (l+r)//2 
            if nums[l] < nums[r] :
                return nums[l]
            
            # left part is sorted 
            if nums[l] <= nums[mid]:
                smallest = min(nums[l],smallest)
                l = mid + 1
            
            # right part is sorted 
            else :
                smallest = min(nums[mid], smallest)
                r = mid
        
        return smallest