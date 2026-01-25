class Solution:
    def compress(self, chars) -> int:
        l, r, i, length, res, n = 0, 0, 0, 0, 0, len(chars)
        while r <= n:
            if r < n and chars[l] == chars[r]:
                r += 1
            else:
                length = r - l 
                chars[i] = chars[l]
                res += 1
                i += 1
                if length > 1:
                    stack = []
                    while length > 9 and length // 10 != 0:
                        stack.append(length % 10)
                        length = length // 10
                    stack.append(length)
                    while stack:
                        chars[i] = str(stack.pop())
                        res += 1
                        i += 1
                if r == n:
                    r += 1
                l = r
        return res, chars
    
chars = ["a","a","b","b","c","c","c"]

chars = ["a"]
s = Solution()
print(s.compress(chars))
            
