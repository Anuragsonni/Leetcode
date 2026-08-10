class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # win = set()
        # for i, val in enumerate(nums):
        #     if val in win :
        #         return True
        #     win.add(val)
        #     if len(win)>k:
        #         win.remove(nums[i-k])
            
        # return False

        if k == 0 :
            return False
        win = set()
        for i in range(len(nums)):
            if nums[i] in win:
                return True
            if len(win)>=k:
                win.remove(nums[i-k])
            win.add(nums[i])
        
        return False

        # win = 0
        # seen = {}
        # for i, val in enumerate(nums):
        #     if val in seen:
        #         if abs(i-seen[val]) <= k:
        #             return True
        #         else:
        #             seen[val] = i
        #     else:
        #         seen[val] = i 
        # return False
            