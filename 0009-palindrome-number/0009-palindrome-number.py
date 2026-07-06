class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x<0 or (x%10 == 0 and x!=0):
        #     return False
        # else :
        #     rev=0
        #     while rev < x:
        #         rev= rev*10+ x%10
        #         x=x//10
        #     return rev == x or rev // 10 == x
        # else :
        x=str(x)
        rev= x[::-1]
        if x==rev:
            return True
        else:
            return False