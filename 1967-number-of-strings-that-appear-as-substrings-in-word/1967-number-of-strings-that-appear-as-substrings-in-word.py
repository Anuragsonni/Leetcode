class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        result=0
        for p in patterns:
            if p in word:
                result+=1
        return result