class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter

        c = Counter(arr)
        visited = set()
        for k, v in c.items():
            if v in visited:
                return False
            visited.add(v)
        return True