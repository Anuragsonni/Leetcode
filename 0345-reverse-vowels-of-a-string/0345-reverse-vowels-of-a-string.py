class Solution:
    def reverseVowels(self, s: str) -> str:
        # ch="".join(filter(self.is_vow, s))
        seen= []
        index=set()
        for i, ch in enumerate(s):
            if self.is_vow(ch):
                seen.append(ch)
                index.add(i)
        ch=["#"]*len(s)
        for i in range(len(s)):
            if i in index:
                ch[i]= seen[-1]
                seen.pop()
            else:
                ch[i]=s[i]

        return "".join(ch)


    def is_vow(self,ch):
        vowel=["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        return ch in vowel