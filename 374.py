# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass
class Solution:
    def guessNumber(self, n: int) -> int:
        g = guess(n)
        if g == 0:
            return n
        if g > 0:
            return self.guessNumber(n+1)
        elif g < 0:
            return self.guessNumber(n//2)
