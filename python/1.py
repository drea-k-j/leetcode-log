# Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# My thoughts: obviously it'd be better to get it under O(n^2), but this is fine for now.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            difference = target - nums[index]
            if difference in nums[index+1:]:
                second_index = nums[index+1:].index(difference) + index + 1
                return [index, second_index]

