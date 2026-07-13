class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if not s:
        #     return 0

        # win=[]
        # maxl=0
        # for ch in s:
        
        #     if ch not in win:
        #         win.append(ch)

        #     else:
        #         while ch in win:
        #             win.pop(0)
        #         win.append(ch)
            
        #     maxl=max(len(win), maxl)
            
        # return maxl

        seen=set()
        l=0
        maxl=0
        for r in range(len(s)):

            while s[r] in seen:
                seen.remove(s[l])
                l+=1 
                
            seen.add( s[r])

            maxl= max(maxl,r-l+1)
        
        return maxl