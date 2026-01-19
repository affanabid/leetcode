class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        n = len(s)
        i = n-1
        while i >= 0:
            if s[i] == ' ':
                i -= 1
            else:
                j = i + 1
                while i >= 0 and s[i] != ' ':
                    i -= 1
                temp = s[i+1:j]
                res += f'{temp} '
        if s[0] == ' ':
            return res[:len(res)-1]
        else:
            return res

s = "the sky is blue"
s = "  hello world  "
s = "a good   example"
sol = Solution()
print(sol.reverseWords(s))