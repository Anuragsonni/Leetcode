class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        l=len(nums)
        lsum, rsum = 0, sum(nums)
        for pivot, val in enumerate(nums):

            rsum-= val
            
            if lsum==rsum:
                return pivot
            else:
                lsum+= val
                
            
        return -1


        # l=len(nums)
        # pivot=l//2-1
        
        # i, lsum, rsum = 0, 0, 0

        # while True:
        #     for j in range(pivot):
        #         lsum+= nums[j]
        #     for j in range(pivot+1,l):
        #         rsum+= nums[j]
        #     if i>pivot+2:
        #         break
        #     elif lsum>rsum :
        #         pivot-=1
        #     elif rsum>lsum :
        #         pivot+=1
        #     else:
        #         return pivot

        #     i+=1
        # return-1