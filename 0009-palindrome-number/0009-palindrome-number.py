class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x%10 == 0 and x!=0):
            return False
        else :
            rev=0
            while rev < x:
                rev= rev*10+ x%10
                x=x//10
            if rev == x:
                return True
            else :
                rev=rev//10
                return True if rev==x else False