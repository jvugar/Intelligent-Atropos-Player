#Vugar Javadov
#U66070335
#jvugar@bu.edu 
#CS440: PA3


import sys
# print to stderr for debugging purposes
# remove all debugging statements before submitting your code
msg = "Given board " + sys.argv[1] + "\n";
sys.stderr.write(msg);

#parse the input string, i.e., argv[1]
s = sys.argv[1]
#s ="[13][302][1003][30002][100003][3000002][10000003][300000002][12121212]LastPlay:null"
(initBoard, lastPlay) = s.split("LastPlay:")

if lastPlay != "null":
	lastPlay = lastPlay[1:]
	lastPlay = lastPlay[:-1]
	lastPlay = lastPlay.split(",")
	lastPlay = [int(i) for i in lastPlay]
   
brd = []
rw = []
for character in initBoard:
	if character  == '[':
            rw = []
	elif character == ']':
            brd.append(rw)
	else:
            rw.append(int(charecter))
brd.reverse()
		


#perform intelligent search to determine the next move
		
#define colors
nocolor = 0
red = 1
blue = 2
green = 3
 
#define size
size = len(brd)-2
          
#define depth
depth = 5

positiveNum = 1000    #upperbound for beta
negativeNum = -1000   #lowerbound for alpha

#find adjacent positions
def adjacent(board, lastPlay):
    rght = lastPlay[2]
    adjacent = []
    hght = lastPlay[1]
    
    
    if hght > 1:
        adjacent = [(hght+1, rght -1), (hght+1, rght), (hght, rght+1), (hght-1, rght+1), (hght-1, rght), (hght, rght-1)]
    else:
        adjacent = [(hght+1, rght -1), (hght+1, rght), (hght, rght+1), (hght-1, rght), (hght-1, rght-1), (hght, rght-1)]

    return adjacent



#find all available moves
def availableMoves(board, lastPlay):
    adjacentList = adjacent(board, lastPlay)
    options = []
    for (h, r) in adjacentList:
        if board[h][r] == 0:
            options.append((h, r))
    if options == []:
        for irow, row in enumerate(board):
            for icol, circle in enumerate(row):
                if circle == 0:
                    options.append((irow, icol))
    return options




#decide whether a move will lose the game            
def gamedone(board, move):
    clr = move[0]
    adjacentList = adjacent(board, move)
    
    for i, (h, r) in enumerate(adjacentList):
        clrs = [color]
        if brd[h][r] != 0:
            clrs.append(board[h][r])
        (H, R) = adjacentList[(i+1) % len(adjacentList)]
        if brd[H][R] != 0:
            clrs.append(board[H][R])
        if len(set(clrs)) == 3:
            return True
    return False


        
#the static evaluator
def evaluator(board, move):
    if (gamedone(board, move)):
        return (negativeNum, [])
    
    score = 0
    
    #get 5 points for each adj with color
    #get 2 points for each pair of adj that have the same color
    #subtract 1 points for each adj that have the same color with move itself
    adjacentList = adjacent(board, move)
    color = move[0]
    for i,  (h, r) in enumerate(adjacentList):
        fill = board[h][r]
        if fill != 0:
            score += 10
            if fill == color:
                score -= 1
            (H, R) = adjList[(1+i) % len(adjList)]
            if fill != board[H][R]:
                score += 5
    return (score, move)
    

#use minimax with alpha beta pruning to search best move
def alphaBetaPrune(board, lastPlay, depth, alpha, beta, isMax):
    #if it is the first move, play it in the top of board
    if lastPlay == "null":
        return (0, [3, SIZE, 1, 1])
    
    if depth == 0 or gamedone(board, lastPlay):
        return evaluator(board, lastPlay)
    else:
        nodes = possibleMoves(board, lastPlay)
        if isMax:
            score = (negativeNum, [])
            for (h, r) in nodes:
                for color in range(1, 4):
                    board[h][r] = color
                    move = [color, h, r, SIZE+2-h-r]
                    nodeScore = alphaBeta(board, move, depth-1, alpha, beta, False)
                    board[h][r] = 0
                    if nodeScore[0] >= score[0]:
                        score = (nodeScore[0], move)
                    if score[0] > alpha:
                        alpha = score[0]
                    if beta <= alpha:
                        break
            
        else:
            score = (positiveNum, [])
            
            for (h, r) in nodes:
                for color in range(1, 4):
                    board[h][r] = color
                    move = [color, h, r, SIZE+2-h-r]
                    nodeScore = alphaBeta(board, move, depth-1, alpha, beta, True)
                    board[h][r] = 0
                    if nodeScore[0] >= score[0]:
                        score = (nodeScore[0], move)
                    if score[0] < beta:
                        beta = score[0]
                    if beta <= alpha:
                        break
            
    return score


#best move
bstMv = alphaBetaPrune(brd, lastPlay, depth, negativeNum, positiveNum, True)
nxtMv = map(str, bstMv[1])
mkMv = ",".join(nxtMv)
        
        
        
        
        
        
#print to stdout for AtroposGame
sys.stdout.write("(" + mkMv + ")");

