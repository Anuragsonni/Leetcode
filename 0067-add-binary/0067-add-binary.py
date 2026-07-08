class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        an=""
        carry=0
        n= max(len(a),len(b))
        while n>min(len(a),len(b)) :
            if len(a)< len(b) :
                a="0"+ a
            else:
                b="0"+ b
        for i in range(n-1,-1,-1) :
            total= int(a[i])+int(b[i])+ carry
            if total==3:
                an="1"+an
                carry=1
            elif total==2:
                an="0"+an
                carry=1
            elif total==1:
                an="1"+an
                carry=0
            else:
                an="0"+an
                carry=0  
        if carry== 1:
            an="1"+an
        return an
        # multi=0
        # ans=0
        # an=""
        # for i in range(len(a)-1,-1,-1):
        #     if a[i]=='1':
        #         ans+=2**multi
        #     multi+=1
        # multi=0
        # for i in range(len(b)-1,-1,-1):
        #     if b[i]=='1':
        #         ans+=2**multi
        #     multi+=1
        # if ans==0:
        #     return "0"
        # while ans>0:
        #     r=ans%2
        #     if r==1:
        #         an+='1'
        #     else:
        #         an+='0'
        #     ans=ans//2
        # return an[::-1]