class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        maxheight= height
        for i in gain:
            height+= i 
            maxheight= max(height, maxheight)
        
        return maxheight