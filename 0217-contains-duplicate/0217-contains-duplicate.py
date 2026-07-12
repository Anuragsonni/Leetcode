class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # while nums:
        #     check= nums.pop()
        #     if check in nums:
        #         return True
        # return False

        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        
        # return False
        return len(nums)!=len(set(nums))