class Solution(object):
    def solve(self, board):

        # n represents the number of rows in board
        n = len(board)

        # m represents the number of columns in board
        m = len(board[0])

        # visited matrix to keep a track of all the blocks that were visited in previous iterations
        vis = [[0 for i in range(m+1)] for j in range(n+1)]

        # changing all 'O's to '@'s which are reachable from 'O's present on the upper boundary.
        for i in range(m):
            if board[0][i]== 'O':
                board[0][i] = '@'
                self.change(board, vis, n, m, 0, i)

        # changing all 'O's to '@'s which are reachable from 'O's present on the lower boundary.
        for i in range(m):
            if board[n-1][i] == 'O':
                board[n-1][i] = '@'
                self.change(board, vis, n, m, n-1, i)

        # changing all 'O's to '@'s which are reachable from 'O's present on the left boundary.
        for i in range(n):
            if board[i][0]== 'O':
                board[i][0] = '@'
                self.change(board, vis, n, m, i, 0)

        # changing all 'O's to '@'s which are reachable from 'O's present on the right boundary.
        for i in range(n):
            if board[i][m-1]== 'O':
                board[i][m-1] = '@'
                self.change( board, vis, n, m, i, m-1)
    
        # changing 'O's that were unreachable from 'O's present on the boundaries to 'X' as they will be surrounded by 'X's
        # changing the '@'s that originally represent 'O's back to 'O' as they are not part of any surrounded region.
        for i in range(n):
            for j in range(m):
                if board[i][j]=='O':
                    board[i][j] = 'X'

                if board[i][j]=='@':
                    board[i][j]='O'


    # change funtion that works on the concept of DFS(depth first search)
    # it changes all the 'O's to '@'s that are reachable from the boundary 'O's
    def change(self, board, vis, n, m, i, j):
        
        if (i<0 or j<0 
            or i>n-1 or j>m-1 
            or vis[i][j]==True   
            or board[i][j]=='X'):
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