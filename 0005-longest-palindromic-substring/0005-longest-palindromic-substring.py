class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n <= 1 or s == s[::-1]:
            return s

        start = 0
        longest_length = 1

        for end in range(1, n):

            even_start = end - longest_length
            odd_start = even_start - 1

            odd_candidate = s[odd_start : end + 1]
            even_candidate = s[even_start : end + 1]

            if odd_start >= 0 and odd_candidate == odd_candidate[::-1]:
                start = odd_start
                longest_length += 2

            elif even_candidate == even_candidate[::-1]:
                start = even_start
                longest_length += 1

        return s[start : start + longest_length]


        # res=""
        # reslen=0
        # for i in range(len(s)):
        #     # for even palandrome
        #     r, l = i + 1, i 

        #     while l>-1 and r<len(s) and (s[l] == s[r]):
        #         if r-l+1>reslen:
        #             res= s[l:r+1]
        #             reslen= r-l+1
        #         # update
        #         r, l = r+1, l-1
            
        #     # for odd palandrome
        #     r, l = i, i

        #     while l>-1 and r<len(s) and (s[l] == s[r]):
        #         if r-l+1>reslen:
        #             res= s[l:r+1]
        #             reslen= r-l+1
        #         # update
        #         r, l = r+1, l-1
        
        # return res