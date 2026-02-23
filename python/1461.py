# Given a binary string `s` and an integer `k`, return `true` if every binary code of length `k` is a substring of `s`. Otherwise, return `false`.

# the key: total number of possibilities is 2^k

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        code_set = set()
        # add all substrings to the code_set
        for i in range(len(s)-k+1):
            code_set.add(s[i:i+k])
        print(code_set)
        # check if set size is 2^k
        return len(code_set) >= 2**k
