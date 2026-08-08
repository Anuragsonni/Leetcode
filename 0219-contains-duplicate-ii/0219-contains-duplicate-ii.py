class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win = 0
        seen = {}
        for i, val in enumerate(nums):
            if val in seen:
                if abs(i-seen[val]) <= k:
                    return True
                else:
                    seen[val] = i
            else:
                seen[val] = i 
        return False
            