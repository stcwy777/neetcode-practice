# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lp = 1
        rp = n
        mp = lp + (rp - lp) // 2
        rslt = guess(mp)

        while rslt != 0:
            if rslt == 1:
                lp = mp + 1
            else:
                rp = mp - 1
            mp = lp + (rp - lp) // 2
            rslt = guess(mp)
        return mp
