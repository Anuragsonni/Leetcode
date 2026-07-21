class Solution:
    def arrangeCoins(self, n: int) -> int:
        g = 0
        n = 2*n
        while g**2 +g < n:
            g +=1
        return g-1 if g**2 +g != n else g