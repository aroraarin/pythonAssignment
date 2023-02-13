class SurroundedRegions:
    def eliminateSurroundedRegions(self, board):
        variable_O = 'O'
        vairable_At = '@'
        variable_X = 'X'
        # n represents the number of rows in board
        n = len(board)

        # m represents the number of columns in board
        m = len(board[0])

        # visited matrix to keep a track of all the blocks that were visited in previous iterations
        vis = [[0 for i in range(m+1)] for j in range(n+1)]

        # changing all 'O's to '@'s which are reachable from 'O's present on all four boundaries.
        for i in range(m):
            if board[0][i]== variable_O:
                board[0][i] = vairable_At
                self.change(board, vis, n, m, 0, i)

        for i in range(m):
            if board[n-1][i] == variable_O:
                board[n-1][i] = vairable_At
                self.change(board, vis, n, m, n-1, i)

        for i in range(n):
            if board[i][0]== variable_O:
                board[i][0] = vairable_At
                self.change(board, vis, n, m, i, 0)

        for i in range(n):
            if board[i][m-1]== variable_O:
                board[i][m-1] = vairable_At
                self.change( board, vis, n, m, i, m-1)
    
        # changing 'O's that were unreachable from 'O's present on the boundaries to 'X' as they will be surrounded by 'X's
        # changing the '@'s that originally represent 'O's back to 'O' as they are not part of any surrounded region.
        for i in range(n):
            for j in range(m):
                if board[i][j] == variable_O:
                    board[i][j] = variable_X

                if board[i][j] == vairable_At:
                    board[i][j] = variable_O


    # change funtion that works on the concept of DFS(depth first search)
    def change(self, board, vis, n, m, i, j):
        
        if i<0 or j<0 or i>n-1 or j>m-1 or vis[i][j]==True or board[i][j]=='X':
            return
        
        # mark the current block visited in visited matrix
        vis[i][j]=True;  

        # change the 'O's to '@'s
        if board[i][j] == 'O':
            board[i][j] = '@'
        
        self.change( board, vis, n, m, i-1, j)
        self.change( board, vis, n, m, i, j-1)
        self.change( board, vis, n, m, i+1, j)
        self.change( board, vis, n, m, i, j+1)           


