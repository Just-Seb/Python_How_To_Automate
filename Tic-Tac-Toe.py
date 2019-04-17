theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ', 'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ', 'low-l': ' ', 'low-m': ' ', 'low-r': ' '}

def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])

def testForwinner(winner):
    if theBoard['top-l'] == 'X':
        if theBoard['mid-l'] == 'X':
            if theBoard['low-l'] == 'X':
                winner = 'X'
                return(winner)
    if theBoard['top-m'] == 'X':
        if theBoard['mid-m'] == 'X':
            if theBoard['low-m'] == 'X':
                winner = 'X'
                return(winner)
    if theBoard['top-r'] == 'X':
        if theBoard['mid-r'] == 'X':
            if theBoard['low-r'] == 'X':
                winner = 'X'
                return(winner)
    if theBoard['top-l'] == 'O':
        if theBoard['mid-l'] == 'O':
            if theBoard['low-l'] == 'O':
                winner = 'O'
                return(winner)
    if theBoard['top-m'] == 'O':
        if theBoard['mid-m'] == 'O':
            if theBoard['low-m'] == 'O':
                winner = 'O'
                return(winner)
    if theBoard['top-r'] == 'O':
        if theBoard['mid-r'] == 'O':
            if theBoard['low-r'] == 'O':
                winner = 'O'
                return(winner)


turn = 'X'
winner = 'S'

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move to which space?')
    move = input()
    theBoard[move] = turn
    testForwinner(winner)
    winnerresult = winner
    if winnerresult == 'X':
        print('X is the winner!')
        break
    if winnerresult == 'O':
        print('O is the winner!')
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
print('Cats game!')