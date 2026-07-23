class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x 
        while l<=r :
            mid = (l+r)//2
            sq = mid * mid
            if sq == x :
                return mid
            elif sq > x:
                r=mid-1
            else:
                l=mid+1
        return r
        # if x==0 or x==1:
        #     return x
        # for i in range(1,x+1):
        #     if i*i > x:
        #         return i-1