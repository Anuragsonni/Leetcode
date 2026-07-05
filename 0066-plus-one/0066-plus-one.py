class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        if all(digit==9 for digit in digits):
            for i in range(len(digits)):
                digits[i]=0
            digits.append(1)
        elif digits[0]==9:
            for i in range(len(digits)):
                if digits[i]==9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    break
        else:
            digits[0] += 1
        digits.reverse()
        return digits