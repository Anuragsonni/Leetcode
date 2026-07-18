class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        odd=True if num%2 else False
        l= 0
        r= (num+odd)//2
        while l<=r :

            mid = (l+r)//2
            if mid * mid < num :
                l = mid + 1
            elif mid * mid > num :
                r=mid-1
            else:
                return True

        return False
