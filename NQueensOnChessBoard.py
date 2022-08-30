def create_board(size=8):
    board=[[0]*size for i in range(size)]
    return board
def print_board(board):
    for i in board:
        print(*i)

def solve(board,col):
    
    if col >= len(board):
        
        return True
    for i in range(len(board)):

        if isvalid(board,i,col):
            board[i][col]='Q'
            #print('---------')
            #`print_board(board)

            if solve(board,col+1):
                return True
        
            board[i][col]=0    
            
    return False
    
def isvalid(board,row,col):
    for i in range(col):
        if board[row][i]:
            return False

    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]:
            return False

    for i,j in zip(range(row,len(board),1),range(col,-1,-1)):
        if board[i][j]:
            return False

    return True        
        


board=create_board()

print_board(board)
solve(board,0)
print('----------------------')
print_board(board)
