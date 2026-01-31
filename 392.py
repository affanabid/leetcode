class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x, y = 0, 0
        count = len(s)
        while x < len(s) and y < len(t):
            if s[x] == t[y]:
                count -= 1
                x += 1
                y += 1
            else:
                y += 1
        return count == 0