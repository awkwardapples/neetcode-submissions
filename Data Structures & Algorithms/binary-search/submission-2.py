class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

    
        while l <= r:
            midpoint = ((r + l) // 2)

            if nums[midpoint] > target:
                r = midpoint - 1
            elif nums[midpoint] < target:
                l = midpoint + 1
            elif nums[midpoint] == target:
                return midpoint
        return -1


        