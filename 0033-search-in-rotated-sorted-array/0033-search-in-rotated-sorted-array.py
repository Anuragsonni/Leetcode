class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        rem = r= len(nums)-1
        if rem == 0 and target in nums :
            return 0
        count=0
        while nums[r] < nums[l] :
            end = nums.pop()
            nums.insert(0,end)
            count+=1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return (mid+rem-count+1)%(rem+1)
        
        return -1