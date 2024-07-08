class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        que = deque()
        for i in range(1, n+1):
            que.append(i)
        while len(que) > 1:
            for i in range(k):
                ele = que.popleft()
                que.append(ele)
            que.pop()
        return que[0]

        