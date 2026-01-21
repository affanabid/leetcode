class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        l, c = len(flowerbed), 0
        if l == 1 and flowerbed[0] == 0:
            return True
        for i in range(l):
            if flowerbed[i] == 0:
                if i == 0:
                    if i+1 < l and flowerbed[i + 1] == 0:
                        c += 1
                        flowerbed[i] = 1
                elif i == l-1:
                    if flowerbed[i - 1] == 0:
                        c += 1
                elif flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    c += 1
        return c == n


flowerbed = [1]
n = 2

# flowerbed = [1,0,0,0,1]
# n = 1

s = Solution()
print(s.canPlaceFlowers(flowerbed, n))