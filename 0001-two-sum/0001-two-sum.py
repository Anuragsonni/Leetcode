class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     com = target - nums[i]
        #     for j in range(i+1, len(nums)):
        #         if com == nums[j]:
        #             return [i,j]
        # return []

        seen = {}
        for i, val in enumerate(nums):
            com = target -val
            if com in seen :
                return i, seen[com]
            seen[val] = i