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
        total=0
        for i in range(len(s)):
            total += roman[s[i]]
        subtract= {
            "IV": 2,
            "IX": 2,
            "XL": 20,
            "XC": 20,
            "CD": 200,
            "CM": 200
        }
        for i in range(len(s)-1):
            che =s[i]+s[i+1]
            if che in subtract:
                total -= subtract[che]
        return total