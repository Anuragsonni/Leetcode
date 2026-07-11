class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s= "". join([char.lower() for char in s if char.isalnum()])
        # return s==s[::-1]
        s=s.lower()
        s="".join(filter(str.isalnum, s))
        return s==s[::-1]