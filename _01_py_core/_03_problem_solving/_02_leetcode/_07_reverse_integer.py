'''
If reversing x causes the value to go outside the signed 32-bit integer range, then return 0.
Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321
'''


class Solution:
    def reverse(self, x):
        # aproach - 1
        # s = str(abs(x))
        # rev = int(s[::-1])

        # if rev > 2147483647:
        #     return 0

        # return rev if x > 0 else (rev*-1)
        # aproach 2
        rev, val = 0, 1
        if x < 0:
            val = -1
            x = -1*x

        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10

        return 0 if rev > 2147483647 else (rev*val)


num = Solution()
print(num.reverse(-123))
