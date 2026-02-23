# Given a positive integer `n`, find and return the longest distance between any two adjacent `1`'s in the binary representation of `n`. If there are no two adjacent `1`'s, return `0`.
# Two `1`'s are adjacent if there are only `0`'s separating them (possibly no `0`'s). The distance between two `1`'s is the absolute difference between their bit positions. For example, the two `1`'s in `"1001"` have a distance of 3.

class Solution:
    def binaryGap(self, n: int) -> int:
        n_list = list(str(format(n, 'b')))
        start_index = 0
        max_distance = 0
        for index in range(1, len(n_list)):
            if n_list[index] == "1":
                distance = index - start_index
                if distance > max_distance:
                    max_distance = distance
                start_index = index
        return max_distance

