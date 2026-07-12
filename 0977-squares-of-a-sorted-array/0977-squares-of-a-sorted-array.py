class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num= [x**2 for x in nums]
        return sorted(num)