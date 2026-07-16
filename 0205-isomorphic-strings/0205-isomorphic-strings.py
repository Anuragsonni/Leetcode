class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sd={}
        used=set()
        for i, v in enumerate(s) :
            
            if v in sd:
                if sd[v] != t[i]:
                    return False
            
                
            sd[v] = t[i]
        
        for i in sd.values():

            if i in used:
                return False

            used.add(i)

        return True