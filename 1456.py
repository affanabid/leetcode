class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o','u']
        st = []
        for char in s:
            if char in vowels:
                st.append(1)
            else:
                st.append(0)
        curr = 0
        l, r = 1, k
        for i in range(k):
            if st[i] == 1:
                curr += 1
        res = curr
        while l < len(s) and r < len(s):
            if st[l-1] == 1:
                curr -= 1
            if st[r] == 1:
                curr += 1
            res = max(res, curr)
            l += 1
            r += 1
        return res
    
s = 'leetcode'
k = 3
sol = Solution()
print(sol.maxVowels(s, k))