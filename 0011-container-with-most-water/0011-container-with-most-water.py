class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area =0
        i, j = 0, len(height)-1

        while i<j:
            Height= min(height[i], height[j])
            Area= Height * (j-i)

            if area< Area:
                area= Area 

            if height[i] < height[j]:
                i+=1
            else:
                j-=1
    
        return area