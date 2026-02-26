# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

# Return the array after sorting it.
from typing import List

class OnesChecker:
    def __init__(self, num_digits):
        self.num_digits = num_digits
    def __call__(self, item):
        return format(item, 'b').count("1") + float("." + str(item).rjust(self.num_digits, '0'))

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:            
        num_digits = len(str(max(arr)))
        arr.sort(reverse=False, key=OnesChecker(num_digits=num_digits))
        return arr
