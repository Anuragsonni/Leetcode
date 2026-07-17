MOD = 10**9 + 7
class Solution:

    @staticmethod
    def power( x, n, mod=0):
        if n==0:
            return 1

        powHalf=Solution.power(x, n//2, mod)
        result = (powHalf * powHalf) % mod

        if n % 2 == 1 :
            result = result * x
        
        return result


    def countGoodNumbers(self, n: int) -> int:
        even_count = (n + 1) // 2
        odd_count = n // 2

        return (self.power(5, even_count, MOD) * self.power(4, odd_count, MOD)) % MOD