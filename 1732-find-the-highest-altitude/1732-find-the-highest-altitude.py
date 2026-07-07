class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        height=[]
        heights=0
        for i in gain:
            height.append(heights)
            heights += i
        height.append(heights)
        return max(height)