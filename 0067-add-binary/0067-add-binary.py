class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        multi=0
        ans=0
        an=""
        for i in range(len(a)-1,-1,-1):
            if a[i]=='1':
                ans+=2**multi
            multi+=1
        multi=0
        for i in range(len(b)-1,-1,-1):
            if b[i]=='1':
                ans+=2**multi
            multi+=1
        if ans==0:
            return "0"
        while ans>0:
            r=ans%2
            if r==1:
                an+='1'
            else:
                an+='0'
            ans=ans//2
        return an[::-1]