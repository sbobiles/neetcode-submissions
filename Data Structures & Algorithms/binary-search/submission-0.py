class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #initializing variables
        # L at index 0, R at last index
        l, r = 0, len(nums) - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1