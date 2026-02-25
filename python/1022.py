# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

# The test cases are generated so that the answer fits in a 32-bits integer.
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeafHelper(self, strings: List[str], root: Optional[TreeNode]) -> List[str]:
        new_val = str(root.val)
        # add current val to strings or otherwise formulate strings
        if len(strings) == 0:
            new_strings = [new_val]
        else:
            new_strings = []
            for s in strings:
                new_strings.append(s + new_val)
        # base case
        if root.left == None and root.right == None:
            return new_strings

        # recurse
        left_strings = []
        right_strings = []
        if root.left != None:
            left_strings = self.sumRootToLeafHelper(new_strings, root.left)
        if root.right != None:
            right_strings = self.sumRootToLeafHelper(new_strings, root.right)
        return left_strings + right_strings

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        strings = []
        response = self.sumRootToLeafHelper(strings, root)
        print(response)
        sum = 0
        for item in response:
            sum += int(item, 2)
        return sum
