class Solution:
    def arrangeCoins(self, n: int) -> int:
        guess = 0
        n = 2*n
        def ans(k):
            return k**2 + k 
        while ans(guess) < n:
            guess +=1
        return guess-1 if ans(guess) != n else guess