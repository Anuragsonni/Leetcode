class Solution:
    def reverseVowels(self, s: str) -> str:
        # ch="".join(filter(self.is_vow, s))
        # seen= []
        # index=set()
        # for i, ch in enumerate(s):
        #     if self.is_vow(ch):
        #         seen.append(ch)
        #         index.add(i)
        # ch=["#"]*len(s)
        # for i in range(len(s)):
        #     if i in index:
        #         ch[i]= seen[-1]
        #         seen.pop()
        #     else:
        #         ch[i]=s[i]

        # return "".join(ch)

        l, r = 0, len(s)-1
        ch=["#"]*len(s)
        while l<=r:
            if self.is_vow(s[l]):

                if self.is_vow(s[r]):
                    ch[l], ch[r]=s[r], s[l]
                    l+=1
                    r-=1
                else:
                    ch[r]=s[r]
                    r-=1
            else:
                ch[l]= s[l]
                l+=1

        return "".join(ch)



    def is_vow(self,ch):
        vowel=["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        return ch in vowel