class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # frequency=[0]*26
        # for i in magazine :
        #     frequency[ord(i)- ord('a')-1] += 1

        # for i in ransomNote :
        #     frequency[ord(i)- ord('a')-1] -= 1
        
        # for i in frequency :

        #     if i<0 :
        #         return False
        
        # return True

        for i in set(ransomNote) :

            if magazine.count(i) < ransomNote.count(i) :
                return False
        
        return True