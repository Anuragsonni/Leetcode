class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        summ, nn, power = 0, 0, 0
        while n>0:
            r=n%10
            if r == 0:
                n=n//10
            elif r != 0:
                multiplyer=pow(10,power)
                nn = multiplyer*r+ nn
                summ += r
                power += 1
                n = n//10
        return summ*nn
            