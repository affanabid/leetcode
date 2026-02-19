from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in range(len(asteroids)):
            exploded = False
            if asteroids[i] >= 0:
                st.append(asteroids[i])
            else:
                while st and st[-1] >= 0:
                    curr = abs(st.pop())
                    if curr > abs(asteroids[i]):
                        st.append(curr)
                        break
                    elif curr == abs(asteroids[i]):
                        exploded = True
                        break
                if (not st or (st and st[-1] < 0)) and not exploded:
                    st.append(asteroids[i])
        return st

asteroids = [5,10,-5]
asteroids = [10,2,-5]
asteroids = [3,5,-6,2,-1,4]
asteroids = [8,-8]
s = Solution()
print(s.asteroidCollision(asteroids))