class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        frequency= {}
        for i, ch in enumerate(s):
            if ch not in frequency:
                frequency[ch] = [0,i]
            else:
                frequency[ch][0] +=1
        for ch in frequency :
            if not frequency[ch][0]:
                return frequency[ch][1]
        return -1