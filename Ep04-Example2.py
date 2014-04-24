#Tic Tac Toe v002
import random
def drawboard():
    print
    print " %s| %s| %s" % (board[1],board[2],board[3])
    print "__|__|__"
    print " %s| %s| %s" % (board[4],board[5],board[6])
    print "__|__|__"
    print " %s| %s| %s" % (board[7],board[8],board[9])
    print
    return
   
 
def iswinner(test):
    if board[1] == test and board[2] == test and board[3] == test:
        return True
    if board[4] == test and board[5] == test and board[6] == test:
        return True
    if board[7] == test and board[8] == test and board[9] == test:
        return True
    if board[1] == test and board[4] == test and board[7] == test:
        return True
    if board[2] == test and board[5] == test and board[8] == test:
        return True
    if board[3] == test and board[6] == test and board[9] == test:
        return True
    if board[1] == test and board[5] == test and board[9] == test:
        return True
    if board[7] == test and board[5] == test and board[3] == test:
        return True
    return False
 
def canWin():
 
        if board[1] == "0" and board[2] == "0" and board[3] != "X":
                return 3
        if board[1] == "0" and board[2] != "X" and board[3] == "0":
                return 2
        if board[1] != "X" and board[2] == "0" and board[3] == "0":
                return 1
       
        if board[4] == "0" and board[5] == "0" and board[6] != "X":
                return 6
        if board[4] == "0" and board[5] != "X" and board[6] == "0":
                return 5
        if board[4] != "X" and board[5] == "0" and board[6] == "0":
                return 4
       
        if board[7] == "0" and board[8] == "0" and board[9] != "X":
                return 9
        if board[7] == "0" and board[8] != "X" and board[9] == "0":
                return 8
        if board[7] != "X" and board[8] == "0" and board[9] == "0":
                return 7
       
        if board[1] == "0" and board[4] == "0" and board[7] != "X":
                return 7
        if board[1] == "0" and board[4] != "X" and board[7] == "0":
                return 4
        if board[1] != "X" and board[4] == "0" and board[7] == "0":
                return 1
       
        if board[2] == "0" and board[5] == "0" and board[8] != "X":
                return 8
        if board[2] == "0" and board[5] != "X" and board[8] == "0":
                return 5
        if board[2] != "X" and board[5] == "0" and board[8] == "0":
                return 2
       
        if board[3] == "0" and board[6] == "0" and board[9] != "X":
                return 9
        if board[3] == "0" and board[6] != "X" and board[9] == "0":
                return 6
        if board[3] != "X" and board[6] == "0" and board[9] == "0":
                return 3
       
        if board[1] == "0" and board[2] == "0" and board[3] != "X":
                return 3
        if board[1] == "0" and board[2] != "X" and board[3] == "0":
                return 2
        if board[1] != "X" and board[2] == "0" and board[3] == "0":
                return 1
       
        if board[4] == "0" and board[5] == "0" and board[6] != "X":
                return 6
        if board[4] == "0" and board[5] != "X" and board[6] == "0":
                return 5
        if board[4] != "X" and board[5] == "0" and board[6] == "0":
                return 4
       
        if board[7] == "0" and board[8] == "0" and board[9] != "X":
                return 9
        if board[7] == "0" and board[8] != "X" and board[9] == "0":
                return 8
        if board[7] != "X" and board[8] == "0" and board[9] == "0":
                return 7
       
        if board[1] == "0" and board[2] == "0" and board[3] != "X":
                return 3
        if board[1] == "0" and board[2] != "X" and board[3] == "0":
                return 2
        if board[1] != "X" and board[2] == "0" and board[3] == "0":
                return 1
       
        if board[1] == "0" and board[5] == "0" and board[3] != "X":
                return 3
        if board[1] == "0" and board[5] != "X" and board[3] == "0":
                return 5
        if board[1] != "X" and board[5] == "0" and board[3] == "0":
                return 1
       
        if board[7] == "0" and board[5] == "0" and board[3] != "X":
                return 3
        if board[7] == "0" and board[5] != "X" and board[3] == "0":
                return 5
        if board[7] != "X" and board[5] == "0" and board[3] == "0":
                return 7
               
        return False
 
def blockMove():
 
        if board[1] == "X" and board[2] == "X" and board[3] != "0":
                return 3
        if board[1] == "X" and board[2] != "0" and board[3] == "X":
                return 2
        if board[1] != "0" and board[2] == "X" and board[3] == "X":
                return 1
       
        if board[4] == "X" and board[5] == "X" and board[6] != "0":
                return 6
        if board[4] == "X" and board[5] != "0" and board[6] == "X":
                return 5
        if board[4] != "0" and board[5] == "X" and board[6] == "X":
                return 4
       
        if board[7] == "X" and board[8] == "X" and board[9] != "0":
                return 9
        if board[7] == "X" and board[8] != "0" and board[9] == "X":
                return 8
        if board[7] != "0" and board[8] == "X" and board[9] == "X":
                return 7
       
        if board[1] == "X" and board[4] == "X" and board[7] != "0":
                return 7
        if board[1] == "X" and board[4] != "0" and board[7] == "X":
                return 4
        if board[1] != "0" and board[4] == "X" and board[7] == "X":
                return 1
       
        if board[2] == "X" and board[5] == "X" and board[8] != "0":
                return 8
        if board[2] == "X" and board[5] != "0" and board[8] == "X":
                return 5
        if board[2] != "0" and board[5] == "X" and board[8] == "X":
                return 2
       
        if board[3] == "X" and board[6] == "X" and board[9] != "0":
                return 9
        if board[3] == "X" and board[6] != "0" and board[9] == "X":
                return 6
        if board[3] != "0" and board[6] == "X" and board[9] == "X":
                return 3
       
        if board[1] == "X" and board[2] == "X" and board[3] != "0":
                return 3
        if board[1] == "X" and board[2] != "0" and board[3] == "X":
                return 2
        if board[1] != "0" and board[2] == "X" and board[3] == "X":
                return 1
       
        if board[4] == "X" and board[5] == "X" and board[6] != "0":
                return 6
        if board[4] == "X" and board[5] != "0" and board[6] == "X":
                return 5
        if board[4] != "0" and board[5] == "X" and board[6] == "X":
                return 4
       
        if board[7] == "X" and board[8] == "X" and board[9] != "0":
                return 9
        if board[7] == "X" and board[8] != "0" and board[9] == "X":
                return 8
        if board[7] != "0" and board[8] == "X" and board[9] == "X":
                return 7
       
        if board[1] == "0" and board[2] == "0" and board[3] != "0":
                return 3
        if board[1] == "0" and board[2] != "X" and board[3] == "X":
                return 2
        if board[1] != "X" and board[2] == "0" and board[3] == "X":
                return 1
       
        if board[1] == "X" and board[5] == "X" and board[3] != "0":
                return 3
        if board[1] == "X" and board[5] != "0" and board[3] == "X":
                return 5
        if board[1] != "0" and board[5] == "X" and board[3] == "X":
                return 1
       
        if board[7] == "X" and board[5] == "X" and board[3] != "0":
                return 3
        if board[7] == "X" and board[5] != "0" and board[3] == "X":
                return 5
        if board[7] != "0" and board[5] == "X" and board[3] == "X":
                return 7
               
        return False
       
#Start of main game.
#
game = 0
random.seed()
while (game == 0):
 
    board = ["-","1","2","3","4","5","6","7","8","9"]
    print "Welcome to Tic Tac Toe"
    print
    player1 = raw_input("Player ones name? ")
    player2 = raw_input("player two's name? (type 'python' for computer appoinante) ")
    movesplayed = 0
    playersturn = 1
    gamewon = False
    while (movesplayed < 9):
        drawboard()
        if playersturn == 1:
            nextmove = raw_input("Your Move %s ? " % (player1))
            if board[(int(nextmove))] == nextmove:
                board[(int(nextmove))] = "X"
                if iswinner("X"):
                    gamewon = True
                    winner = player1
                    break
                playersturn = 0
                movesplayed = movesplayed+1
            else:
                print "the move was invalid or space has been taken"
        else:
            if player2.lower() == "python":
                                checkWin = canWin()
                                stopwin = blockMove()
                                if checkWin == False:
                                        if stopwin == False:
                                                nextmove = str(random.randrange(1,9))
                                        else:
                                                nextmove = str(stopwin)
                                        print "Pythons move was %s " % (nextmove)
                                else:
                                        nextmove = str(checkWin)
                                        print "Pythons move was %s " % (nextmove)
            else:
                nextmove = raw_input("Your Move %s ? " % (player2))
            if board[(int(nextmove))] == nextmove:
                board[(int(nextmove))] = "0"
                if iswinner("0"):
                    gamewon = True
                    winner = player2
                    break
                playersturn = 1
                movesplayed = movesplayed+1
            else:
                print "the move was invalid or space has been taken"
       
    if gamewon:
                drawboard()
                print "congratulations %s you won this game" % winner
                print
    else:
        print "Oh well %s the game with %s was a draw....." % (player1,player2)
        print
    print
   
    if  raw_input("Play again? ( Y or N) ").lower() == 'n':
        game = 1
   
print "Good bye!"
