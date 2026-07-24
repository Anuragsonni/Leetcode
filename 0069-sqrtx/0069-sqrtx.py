class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l<=r :
            mid = (l+r) // 2 
            sq = mid * mid 
            if sq > x:
                r = mid - 1 
            elif sq < x:
                l = mid +1 
            else:
                return mid
        return r