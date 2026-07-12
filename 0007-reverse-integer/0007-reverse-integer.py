class Solution:
    def reverse(self, x: int) -> int:
        # negetive= x<=0
        # x= str(abs(x))
        # x= int(x[::-1])

        # if negetive:
        #     x= -x
        
        # if x > 2147483647 or x < -2147483648:
        #     return 0

        # return x



        
        negetive= x<=0
        x= abs(x) 
        ans=0

        while x>0:
            ans= ans*10 +x%10 
            x=x//10

            if ans > 2147483647 :
                return 0
        
        if negetive:
            ans = -ans

        return ans