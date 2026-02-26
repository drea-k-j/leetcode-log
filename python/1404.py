# Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
# If the current number is even, you have to divide it by 2.
# If the current number is odd, you have to add 1 to it.
# It is guaranteed that you can always reach one for all test cases.

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        s_len = len(s)
        while s_len > 1:
            if s[-1] == "0":
                s = s[:-1]
            else:
                carry = 1
                index = s_len - 1
                while carry > 0:
                    # special case if index is -1
                    if index == -1:
                        s = "1" + s
                        break
                    new_sum = int(s[index]) + carry
                    new_num, carry = new_sum % 2, new_sum // 2
                    s = s[:index] + str(new_num) + s[index+1:]
                    index -= 1
            s_len = len(s)
            steps += 1
        return steps