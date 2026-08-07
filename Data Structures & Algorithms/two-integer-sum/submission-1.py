class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}

        for index, number in enumerate(nums):
            complement = target - number
            if complement in seenMap:
                return [seenMap[complement], index]
            seenMap[number] = index
        return