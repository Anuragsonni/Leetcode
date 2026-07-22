class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        smallest = float('inf')  # Use infinity instead of hardcoded 5000

        while l <= r:
            # OPTIMIZATION: If the current range is already sorted,
            # the leftmost element is guaranteed to be the minimum!
            if nums[l] <= nums[r]:
                smallest = min(smallest, nums[l])
                break

            mid = (l + r) // 2
            smallest = min(smallest, nums[mid])

            # Left half is sorted -> smallest in left half is nums[l], search right half
            if nums[mid] >= nums[l]:
                smallest = min(smallest, nums[l])
                l = mid + 1
            # Right half is unsorted/pivot is on the left -> search left half
            else:
                r = mid - 1

        return smallest