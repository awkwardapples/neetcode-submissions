class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) - 1
    
        while r >= l:
            midpoint = int((l + r) / 2)
            if target == nums[midpoint]:
                return midpoint
            else:
                if target > nums[midpoint]:
                    l = midpoint + 1
                else:
                    r = midpoint - 1
        return -1
        
