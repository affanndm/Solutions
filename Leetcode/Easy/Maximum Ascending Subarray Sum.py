from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        final_max = 0

        for index, i in enumerate(nums):
            current_max = i
            previous = i

            for x in nums[index + 1:]:
                if x > previous:
                    current_max += x
                    previous = x
                else:
                    break

            if current_max > final_max:
                final_max = current_max

        return final_max
