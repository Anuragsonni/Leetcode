from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # frequency=[0]* 26
        # for i in text:
        #     frequency[ord(i)-ord('a')] +=1
        # dic = {
        #     'a': frequency[0],
        #     'b': frequency[1],
        #     'l': frequency[11]//2,
        #     'o': frequency[14]//2,
        #     'n': frequency[13]
        # }
        # a=min(dic.values())
        # if a>0:
        #     return a
        # else:
        #     return 0
        count= Counter(text)
        lis=[count['b'],count['a'],count['l']//2,count['o']//2,count['n']]
        ans=min(lis)
        if ans>0:
            return ans
        else:
            return 0
