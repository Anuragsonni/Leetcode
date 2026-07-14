class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in set(s+t) :
            if t.count(i) != s.count(i) :
                return False
        return True