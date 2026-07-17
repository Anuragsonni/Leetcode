class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # if not word1:
        #     return word2
        # if not word2:
        #     return word1
        # result=""
        # i, j = 0, 0
        # for index in range(len(word1)+len(word2)):
        #     if i==len(word1):
        #         return result + word2[j:]
        #     if j==len(word2):
        #         return result + word1[i:]    
            
        #     if index%2 :
        #         result += word2[j]
        #         j+=1
        #     else:
        #         result += word1[i]
        #         i+=1
        
        # return result
        
        result = []
        i = j = 0

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        result.extend(word1[i:])
        result.extend(word2[j:])

        return "".join(result)
