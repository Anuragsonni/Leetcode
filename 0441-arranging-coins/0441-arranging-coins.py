class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1 , n
        n = 2*n
        while l<=r :
            mid = (l+r)//2
            t = mid**2 + mid
            if t == n:
                return mid
            elif t > n:
                r = mid - 1
            else:
                l = mid + 1 
            
        return r