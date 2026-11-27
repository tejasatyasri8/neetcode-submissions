class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        ds = [""] * len(word)

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if (r < 0 or r >= rows or c < 0 or c >= cols):
                return False

            if board[r][c] != word[idx]:
                return False

            # Store current character
            ds[idx] = board[r][c]

            # Mark current cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all four directions
            if (dfs(r+1, c, idx+1) or
                dfs(r-1, c, idx+1) or
                dfs(r, c+1, idx+1) or
                dfs(r, c-1, idx+1)):
                return True

            # Backtrack
            board[r][c] = temp
            ds[idx] = ""

            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False