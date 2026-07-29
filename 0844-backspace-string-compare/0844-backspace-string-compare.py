class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def original(ch):
            real = []
            for i in ch:
                if i == "#":
                    if not real:
                        continue
                    real.pop()
                else :
                    real.append(i)
            return "".join(real)
        
        return original(s) == original(t)