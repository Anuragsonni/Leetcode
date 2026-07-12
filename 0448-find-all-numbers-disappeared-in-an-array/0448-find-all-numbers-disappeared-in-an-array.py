class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=len(nums)
        one2n={x for x in range(1,l+1)}
        nums=set(nums)
        return list(one2n-nums)