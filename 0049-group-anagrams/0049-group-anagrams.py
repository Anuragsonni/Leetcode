# from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # result= defaultdict(list)
        # for word in strs:
        #     freq=[0]*26

        #     for ch in word:
        #         freq[ord(ch)-ord('a')]+=1
            
        #     result[tuple(freq)].append(word)
        
        # return list(result.values())

        result=defaultdict(list)
        for word in strs:
            key="".join(sorted(word))
            result[key].append(word)
        
        return list(result.values())