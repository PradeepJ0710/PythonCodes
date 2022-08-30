def board_creation(size = int(input())):
    board=[[0]*size for i in range(size)]
    return board
	
def board_printing(board):
    for i in board:
        print(*i)

def board_solution(board,col):
    
    if col >= len(board):
        
        return True
    for i in range(len(board)):

        if isValid(board,i,col):
            board[i][col]='Q'
            #print('---------')
            #`board_printing(board)

            if board_solution(board,col+1):
                return True
        
            board[i][col]=0    
            
    return False
    
def isValid(board,row,col):
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
        


board=board_creation()

board_printing(board)
board_solution(board,0)
print('--------------------------------------------')
board_printing(board)
