class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[num] = i
           
        return []

            
