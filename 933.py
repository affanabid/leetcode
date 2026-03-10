from collections import deque
class RecentCounter:

    def __init__(self):
        self.requests = deque()
        self.recent_req = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while t-3000 > self.requests[0]:
            self.requests.popleft()
        self.recent_req = len(self.requests)
        return self.recent_req



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)