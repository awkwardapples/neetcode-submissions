class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:    
        Numbers_visited = set()
        for num in nums:
            if num in Numbers_visited:
                return True
            Numbers_visited.add(num)

        return False

