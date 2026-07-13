class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s=list(s)
        count=sum(self.isvow(c) for c in s[:k])
        if count == k :
            return k
        else:
            maxcount= count

        for i in range(k, len(s)):
            if self.isvow(s[i]):
                count+=1
            if self.isvow(s[i-k]):
                count-=1
            if count == k :
                return k
            elif count > maxcount:
                maxcount= count

        return maxcount
            
        
    def isvow(self, ch):
        return ch in "aeiou"