class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        reslen=0
        for i in range(len(s)):
            # for even palandrome
            r, l = i + 1, i 

            while l>-1 and r<len(s) and (s[l] == s[r]):
                if r-l+1>reslen:
                    res= s[l:r+1]
                    reslen= r-l+1
                # update
                r, l = r+1, l-1
            
            # for odd palandrome
            r, l = i, i

            while l>-1 and r<len(s) and (s[l] == s[r]):
                if r-l+1>reslen:
                    res= s[l:r+1]
                    reslen= r-l+1
                # update
                r, l = r+1, l-1
        
        return res