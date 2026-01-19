class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        n1, n2 = len(word1), len(word2)
        i = 0
        while i < (min(n1, n2)):
            temp = word1[i] + word2[i]
            res += temp
            i += 1
        while i < n1:
            res += word1[i]
            i += 1
        while i < n2:
            res += word2[i]
            i += 1
        return res



word1 = "abc"
word2 = "pqr"

word1 = "ab"
word2 = "pqrs"

word1 = "abcd"
word2 = "pq"

s = Solution()
print(s.mergeAlternately(word1, word2))