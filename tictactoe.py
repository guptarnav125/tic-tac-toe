"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x=0
    o=0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==X:
                x+=1
            if board[i][j]==O:
                o+=1

    if x>o:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available=set()
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==EMPTY:
                available.add((i,j))
    return available



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception
    turn=player(board)
    new=copy.deepcopy(board)
    i,j=action
    new[i][j]=turn
    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] == board[i][1]==board[i][2] !=EMPTY):
            return board[i][0]
        if (board[0][i] == board[1][i]==board[2][i] !=EMPTY):
            return board[0][i]
    if board[0][0]==board[1][1]==board[2][2]!=EMPTY:
        return board[0][0]
    if board[2][0]==board[1][1]==board[0][2]!=EMPTY:
        return board[2][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True

    for row in board:
        if EMPTY in row:
            return False
    return True




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    turn=player(board)
    if turn==X:
        best_move=None
        max_val=float('-inf')
        for action in actions(board):
            value=min_value(result(board,action))
            if value>max_val:
                max_val=value
                best_move=action
        return best_move
    else:
        best_move=None
        min_val=float('inf')
        for action in actions(board):
            value=max_value(result(board,action))
            if value<min_val:
                min_val=value
                best_move=action
        return best_move

def min_value(board):
    if terminal(board):
        return utility(board)
    v=float('inf')
    for action in actions(board):
        v=min(v,max_value(result(board,action)))
    return v
    
def max_value(board):
    if terminal(board):
        return utility(board)
    v=float('-inf')
    for action in actions(board):
        v=max(v,min_value(result(board,action)))
    return v