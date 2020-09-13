# write your code here
# write your code here
# write your code here
import random
import math

def display(list_str):
    print('---------')
    print('|',list_str[0],list_str[1],list_str[2],'|')
    print('|',list_str[3],list_str[4],list_str[5],'|')
    print('|',list_str[6],list_str[7],list_str[8],'|')
    print('---------')

def checkWin(list_str):
    c_match = 0
    c_space = 0
    result = None
    
    if list_str[0] == list_str [1] and list_str[1] == list_str[2] and list_str[0] != empty_space and list_str[1] != empty_space and list_str[2] != empty_space:
        result = list_str[0]
        c_match += 1
    if list_str[3] == list_str [4] and list_str[4] == list_str[5] and list_str[3] != empty_space and list_str[4] != empty_space and list_str[5] != empty_space:
        result = list_str[3]
        c_match += 1
    if list_str[6] == list_str [7] and list_str[7] == list_str[8] and list_str[6] != empty_space and list_str[7] != empty_space and list_str[8] != empty_space:
        result = list_str[6]
        c_match += 1
    if list_str[0] == list_str [3] and list_str[3] == list_str[6] and list_str[0] != empty_space and list_str[3] != empty_space and list_str[6] != empty_space:
        result = list_str[0]
        c_match += 1
    if list_str[1] == list_str [4] and list_str[4] == list_str[7] and list_str[1] != empty_space and list_str[4] != empty_space and list_str[7] != empty_space:
        result = list_str[1]
        c_match += 1
    if list_str[2] == list_str [5] and list_str[5] == list_str[8] and list_str[2] != empty_space and list_str[5] != empty_space and list_str[8] != empty_space:
        result = list_str[2]
        c_match += 1
    if list_str[0] == list_str [4] and list_str[4] == list_str[8] and list_str[0] != empty_space and list_str[4] != empty_space and list_str[8] != empty_space:
        result = list_str[0]
        c_match += 1
    if list_str[6] == list_str [4] and list_str[4] == list_str[2] and list_str[6] != empty_space and list_str[4] != empty_space and list_str[2] != empty_space:
        result = list_str[6]
        c_match += 1

    if c_match == 1:
        result += ' wins'
        playturn = False
    elif c_match > 1:
        result = 'Impossible'
        playturn = False
    elif c_match == 0 and move == 9:
        numX = 0
        numY = 0

        for i in list_str:
            if i == 'X':
                numX += 1
            if i == 'O':
                numY += 1
            if i == '_' or i == ' ':
                c_space += 1

        diffXY = abs(numX - numY)
        print(diffXY)
        print(c_space)
        if diffXY == 1 and c_space == 0:
            result = 'Draw'
        if c_space > 0:
            result = 'Game not finished'
        if diffXY > 1 :
        #    print('play')
            result = 'Impossible'

    return result

def playerInput(player, p1Mode, p2Mode):
    coord = None
    while True:
        if p1Mode == 'user' or p2Mode == 'user':
            word = input()
        elif p1Mode == 'easy' or p2Mode == 'easy':
            print('Making move level "' + p1Mode + '"')
            word = compmove(player, p1Mode)           
        elif p1Mode == 'medium' or p2Mode == 'medium':
            print('Making move level "' + p2Mode + '"')
            word =  compmove(player, p2Mode) 
        elif p1Mode == 'hard' or p2Mode == 'hard':
            print('Making move level "' + p1Mode + '"')
            #return bestMove(list_str, player) 
            word =  compmove(player, p2Mode)         

        if word.isalpha():
            print('You should enter numbers!')
            #word = input()
            continue


        print(word)
        XCoord, YCoord = word.split()


        if not XCoord.isnumeric() or not YCoord.isnumeric():
            print('You should enter numbers!')
            #XCoord, YCoord = input().split()
            continue

        #print(XCoord,YCoord)
        if int(XCoord) < 0 or  int(XCoord) > 3 or int(YCoord) < 0 or  int(YCoord) > 3:
            print('Coordinates should be from 1 to 3!')
            #XCoord, YCoord = input().split()
            continue
        #if p1Mode != 'hard'
        coord = (int(XCoord) - 1)  + (9 - (3 * int(YCoord)))
        if list_str[coord] == 'X' or list_str[coord] == 'O':
            print('This cell is occupied! Choose another one!')
        # XCoord, YCoord = input().split()
        else:
            print('coord inside' + str(coord))
            break
    if player == 'X':
        player = 'O'
    else:
        player = 'X'        
    return coord

def compmove(player, mode):
    '''if mode == 'easy':
        return str(random.randint(1,3)) + ' ' + str(random.randint(1,3))
    elif mode == 'medium':
        #Check two accross
        if list_str[0] == list_str[1] and list_str[0] != empty_space and list_str[1] != empty_space:
            return '3 3'
        elif list_str[1] == list_str[2] and list_str[1] != empty_space and list_str[2] != empty_space:
            return '1 3'
        elif list_str[3] == list_str[4] and list_str[3] != empty_space and list_str[4] != empty_space:
            return '3 2'    
        elif list_str[4] == list_str[5] and list_str[4] != empty_space and list_str[5] != empty_space:
            return '1 2' 
        elif list_str[6] == list_str[7] and list_str[6] != empty_space and list_str[7] != empty_space:
            return '3 1' 
        elif list_str[7] == list_str[8] and list_str[7] != empty_space and list_str[8] != empty_space:
            return '1 1'                                             
        #Check two down
        elif list_str[0] == list_str[3] and list_str[0] != empty_space and list_str[3] != empty_space:
            return '1 1'
        elif list_str[3] == list_str[6] and list_str[3] != empty_space and list_str[6] != empty_space:
            return '1 3'
        elif list_str[1] == list_str[4] and list_str[1] != empty_space and list_str[4] != empty_space:
            return '2 1'    
        elif list_str[4] == list_str[7] and list_str[4] != empty_space and list_str[7] != empty_space:
            return '2 3' 
        elif list_str[2] == list_str[5] and list_str[2] != empty_space and list_str[4] != empty_space:
            return '3 1' 
        elif list_str[5] == list_str[8] and list_str[5] != empty_space and list_str[8] != empty_space:
            return '3 3' 
        #Check two match with one empty space
        elif list_str[0] == list_str[8] and list_str[0] != empty_space and list_str[8] != empty_space:
            return '2 2'
        elif list_str[1] == list_str[7] and list_str[1] != empty_space and list_str[7] != empty_space:
            return '2 2'
        elif list_str[2] == list_str[6] and list_str[2] != empty_space and list_str[6] != empty_space:
            return '2 2'    
        elif list_str[3] == list_str[5] and list_str[3] != empty_space and list_str[5] != empty_space:
            return '2 2' 
        else:
            return str(random.randint(1,3)) + ' ' + str(random.randint(1,3))'''   
    return str(random.randint(1,3)) + ' ' + str(random.randint(1,3))   

def bestMove(list_str, player):
    bestScore = -math.inf
    optMove = None
    for i in range(len(list_str)):
        #check if space is empty
        if list_str[i] == empty_space:
            list_str[i] = player
            score = minimax(list_str, 0, player, False)
            list_str[i] = empty_space
            if score > bestScore:
                bestScore = score
                optMove = i    # should be assign move
    
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return optMove
                            
def minimax(list_str, depth, player, isMaximizing):
    result = checkWin(list_str)
    letter = None
    if result != None:
        letter = result[0]
    print(letter)
    if letter != None:
        if letter != 'I':
            return scores[letter]  #not correct, must change checkWin()
    
    if isMaximizing:
        bestScore = math.inf
        for i in range(len(list_str)):
            if list_str[i] == empty_space:
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'                
                list_str[i] = player
                score = minimax(list_str, depth + 1, player, False)
                list_str[i] = empty_space
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = -math.inf
        for i in range(len(list_str)):
            if list_str[i] == empty_space:
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'                 
                list_str[i] = player
                score = minimax(list_str, depth + 1, player, True)
                list_str[i] = empty_space
                bestScore = min(score, bestScore)
        return bestScore
                               
empty_space = ' '
scores = {'X' : 10, 'O' : -10, 'D' : 0}
result  = None
playturn = True
player = 'X'
move = 0
coord = 0
hard_score = None
start_input = 'None'
list_str = []
for i in range(9):
    list_str.append(' ')
display(list_str)

c = 0
while 'exit' not in start_input:
    while len(start_input) != 3:
        start_input = input().split()
        if 'exit' in start_input:
            break

    if 'exit' in start_input:
        break
    coord = playerInput(player, start_input[1], start_input[2])

    list_str[coord] = player
    print('coord outside' + str(coord))
    print(player)

    display(list_str)
    move += 1
    result = checkWin(list_str)

    if result != None:
        print(result)
        break

#End of game
