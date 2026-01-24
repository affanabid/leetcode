class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U']
        res = []
        l, r = 0, len(s)-1
        res = []
        for char in s:
            res.append(char)
        while l < r:
            if res[l] in vowels and res[r] in vowels:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1
            elif res[l] not in vowels:
                l += 1
            elif res[r] not in vowels:
                r -= 1
        res = ''.join(res)
        return res
            