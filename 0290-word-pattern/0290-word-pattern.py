class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        seen = {}
        s_list= s.split()
        
        if len(pattern)!= len(s_list):
            return False

        for ind, i in enumerate(pattern) :
            if i in seen:
                if seen[i] != s_list[ind]:
                    return False
            seen[i]=s_list[ind]
        v = set()
        for i in seen.values():
            if i in v :
                return False
            v.add(i)
        return True