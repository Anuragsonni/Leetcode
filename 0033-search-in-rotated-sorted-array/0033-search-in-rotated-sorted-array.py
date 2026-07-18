class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l=0
        # rem = r= len(nums)-1
        # if rem == 0 and target in nums :
        #     return 0
        # count=0
        # while nums[r] < nums[l] :
        #     end = nums.pop()
        #     nums.insert(0,end)
        #     count+=1

        # while l<=r:
        #     mid = (l+r)//2
        #     if nums[mid] < target:
        #         l = mid + 1
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         return (mid+rem-count+1)%(rem+1)
        
        # return -1

        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1