class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        for i in range(min(len(str1), len(str2)), 0, -1):
            if self.isDivisor(i, str1, str2):
                return str1[:i]
            
        return ""

    def isDivisor(self, i, str1, str2):
        curr = str1[:i]
        if len(str1) % i or len(str2) % i:
            return False
        f1, f2 = len(str1) // i, len(str2) // i
        if  curr * f1 == str1 and curr * f2 == str2:
            return True
        return False
    
str1 = "ABABAB"
str2 = "ABAB"

str1 = "ABCABC"
str2 = "ABC"

str1 = "AAAAAB"
str2 = "AAA"

s = Solution()
print(s.gcdOfStrings(str1, str2))