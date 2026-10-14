class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])

        def dfs(r,c,idx):
            if(idx>=len(word)):
                return True
            if(r<0 or r>=len(board) or c<0 or c>=len(board[0]) or board[r][c]!=word[idx]):
                return False
            
            temp=board[r][c]
            board[r][c]='#'
            found=(
                dfs(r+1,c,idx+1) or
                dfs(r-1,c,idx+1) or
                dfs(r,c+1,idx+1) or
                dfs(r,c-1,idx+1)
            )
            board[r][c]=temp
            return found
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
        
