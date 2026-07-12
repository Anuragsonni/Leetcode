class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # num= [x**2 for x in nums]
        # return sorted(num)

        # three pointer approch 
        l, r, w = 0, len(nums)-1, len(nums)-1
        lis=[0]*len(nums)
        while l <= r :
            if nums[l]**2 < nums[r]**2:
                lis[w]= nums[r]**2
                r-=1
            else :
                lis[w]= nums[l]**2
                l+=1
            w-=1
            # else :
            #     lis[w], lis[w-1]= nums[r]**2, nums[r]**2
            #     w-=2
            #     l+=1 
            #     r-=1
        return lis