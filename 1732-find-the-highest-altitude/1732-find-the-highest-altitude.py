class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        height=[0]
        heights=0
        for i in gain:
            heights += i
            height.append(heights)
        return max(height)