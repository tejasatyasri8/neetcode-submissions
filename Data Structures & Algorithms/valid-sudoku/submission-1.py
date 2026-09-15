class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        boxes=collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val==".":
                    continue
                box_val=(r//3,c//3)

                if(val in rows[r] or
                    val in cols[c] or
                    val in boxes[box_val]):
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_val].add(val)
        return True

