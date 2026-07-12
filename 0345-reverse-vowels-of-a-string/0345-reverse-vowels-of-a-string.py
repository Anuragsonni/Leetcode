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
        ch=list(s)
        while l<=r:
            if not self.is_vow(s[l]):
                l+=1
            elif not self.is_vow(s[r]):
                r-=1
            else:
                ch[l], ch[r]= ch[r], ch[l]
                l+=1
                r-=1
            

        return "".join(ch)



    def is_vow(self,ch):
        return ch in {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}