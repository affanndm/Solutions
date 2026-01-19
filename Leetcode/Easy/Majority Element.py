class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        seen = []
        for i in nums:
            if i in seen:
                continue
            else:
                seen.append(i)
                if nums.count(i) > n/2:
                    return i
