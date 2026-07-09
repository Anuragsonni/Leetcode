import math 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power=1
        while power<=n:
            if power==n:
                return True
            power*= 2
        return False
        # if n <= 0:
        #     return False

        # b = math.log2(n)
        # return abs(b - round(b)) < 1e-10