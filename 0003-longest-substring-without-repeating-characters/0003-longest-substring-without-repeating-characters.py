class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        win=[]
        maxl=0
        for ch in s:
        
            if ch not in win:
                win.append(ch)

            else:
                while ch in win:
                    win.pop(0)
                win.append(ch)
            
            maxl=max(len(win), maxl)
            
        return maxl