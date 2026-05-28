class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Define sets
        row = defaultdict(set)
        col = defaultdict(set)
        sqr = defaultdict(set)
        
        # Iterate through row
        for i in range(len(board)):
            # Iterate through col
            for j in range(len(board[i])):
                # Check row, col, matrix
                if board[i][j] == '.':
                    continue
                
                if ( board[i][j] in row[i] or
                        board[i][j] in col[j] or
                            board[i][j] in sqr[(i // 3, j // 3)] ):
                    return False

                # Add to sets
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                sqr[(i // 3, j // 3)].add(board[i][j])
        # Return
        return True
        