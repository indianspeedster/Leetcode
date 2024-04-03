class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i,j,k):
            
            if k == len(word):
                return True
            if i not in range(m) or j not in range(n) or board[i][j] != word[k] or (i,j) in visited:
                return False
            
            visited.add((i,j))
            k = dfs(i+1,j,k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1)
            visited.remove((i,j))
            return k
        
        m, n = len(board), len(board[0])
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                
                    if dfs(i,j,0):
                        return True
            
        return False


            
            
            
        

        