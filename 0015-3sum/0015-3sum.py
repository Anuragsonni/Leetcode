class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        siz=len(nums)
        for i in range(siz-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            start=i+1
            end=siz-1
            while start<end:
                total=nums[i]+nums[start]+nums[end]
                if total<0:
                    start+=1
                elif total>0:
                    end-=1
                else:
                    ans.append([nums[i],nums[start],nums[end]])
                    while start<end and (nums[start]== nums[start+1] or nums[end]== nums[end-1]):
                         
                        if nums[start]== nums[start+1]:
                            start+=1 
                        else :
                            end-=1
                    start+=1
                    end-=1
        return ans