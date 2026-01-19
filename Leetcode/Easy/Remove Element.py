class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        for num in nums:
            if num != val:
                nums[x] = num
                x += 1
        return x

