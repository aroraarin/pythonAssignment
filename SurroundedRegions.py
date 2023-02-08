class SurroundedRegions:
    def eliminateSurroundedRegions(self, board):

        # n represents the number of rows in board
        n = len(board)

        # m represents the number of columns in board
        m = len(board[0])

        # visited matrix to keep a track of all the blocks that were visited in previous iterations
        vis = [[0 for i in range(m+1)] for j in range(n+1)]

        # changing all 'O's to '@'s which are reachable from 'O's present on all four boundaries.
        for i in range(m):
            if board[0][i]== 'O':
                board[0][i] = '@'
                self.change(board, vis, n, m, 0, i)

        for i in range(m):
            if board[n-1][i] == 'O':
                board[n-1][i] = '@'
                self.change(board, vis, n, m, n-1, i)

        for i in range(n):
            if board[i][0]== 'O':
                board[i][0] = '@'
                self.change(board, vis, n, m, i, 0)

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


#validator to check whether input row is valid or not
def validator(str):
    for i in str:
        if  i != " " and i!='X'and i!='O':
            return False
    return True        


try:
    #initialising board 
    board = []

    numOfRows = int(input("Enter number of rows. "))
    numOfCols = int(input("Enter number of columns. "))

    #rowCount to track current row
    rowCount = 1

    #flag to check if given input is valid
    flag = False

    #taking input in board
    for i in range(numOfRows):
        temp = []
        flag = False
        while(flag==False):
            print(f"Enter row number {rowCount}")
            currentRow = input()
            temp = currentRow.split(" ")

            #if user enters "quit" program execution will stop
            if currentRow=="quit":
                break
            #checking if the input is invalid
            elif(len(temp)!=numOfCols or validator(currentRow)==False):
                print("Enter valid input.")
            #if corrent input then move to next iteration
            else:
                flag = True    
        
        if(flag==False):
            break

        print(f"Added row number {rowCount}")
        rowCount+=1
        board.append(temp)

    #checking if user opted to quit the program
    if(flag):
        print("Your input: ")
        for i in board:
            print(i)

        sol = SurroundedRegions()

        #calling elinateSurroundedRegions funtion from SurroundedRegions class
        sol.eliminateSurroundedRegions(board)
        print("After removing surrounded O regions: ")
        for i in board:
            print(i)

except Exception as e:
    print(e)
