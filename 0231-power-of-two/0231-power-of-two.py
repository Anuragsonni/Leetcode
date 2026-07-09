class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power=1
        while power<=n:
            if power==n:
                return True
            power*= 2
        return False