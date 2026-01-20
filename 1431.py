class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [None] * len(candies)
        mx = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= mx:
                res[i] = True
            else:
                res[i] = False
        return res