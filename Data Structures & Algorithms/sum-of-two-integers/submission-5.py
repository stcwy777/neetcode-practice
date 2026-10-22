class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAXINT = 0x7FFFFFFF

        carry = b
        res = a

        while carry:
            new_carry = ((res & carry) << 1) & MASK
            res = (res ^ carry) & MASK
            carry = new_carry

        if res > MAXINT:
            return ~(res ^ MASK)
        else:
            return res