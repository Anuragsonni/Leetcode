class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for num in nums:
            temp=[]
            while num>0:
                temp.append(num%10)
                num=num//10
            temp.reverse()
            ans.extend(temp)
        return ans
        # for num in nums:
        #     ans.extend(int(s) for s in str(num))
        # return ans