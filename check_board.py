from board import Board

def checking_board(self,num1,num2):
    if Board.board[(num1+1)*3+1][(num2+1)*6+3] == ' ':
        return 'empty'
    if Board.board[(num1+1)*3+1][(num2+1)*6+3] == '/':
        return 'Mountain'
    if Board.board[(num1+1)*3+1][(num2+1)*6+3] == '$':
        return 'Coin'
    if Board.board[(num1+1)*3+1][(num2+1)*6+3] == '()':
        return 'Cloud'
    if Board.board[(num1+1)*3+1][(num2+1)*6+3] == '#':
        return 'Brick'
    #if Board.board[num1][num2] == '$':
    return 'lol'
    