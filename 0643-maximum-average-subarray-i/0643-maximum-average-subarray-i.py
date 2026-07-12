class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        window=sum(nums[:k])
        maxsum=window
        l=len(nums)

        for i in range(l-k):
            window = window + nums[i+k] - nums[i]
            if window > maxsum:
                maxsum=window
        
        return float(maxsum)/k