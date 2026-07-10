class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # return haystack.find(needle)

        # special case if needle length is 0 
        if needle == "":
            return -1

        for start in range(len(haystack)- len(needle)+1) :
            match= True 
            
            for i in range(len(needle)) :
                if haystack[start+i] != needle[i]:
                    match =False
                    break
            
            if match:
                return start
        
        return -1