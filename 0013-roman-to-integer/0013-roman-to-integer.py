class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman= {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        integer=roman[s[-1]]
        for i in range(len(s)-1,0,-1):
            if  roman[s[i]] <=roman[s[i-1]]:    #right < left
                integer += roman[s[i-1]]
            else:
                integer -= roman[s[i-1]]

        return integer