


""" Go to FineBestAction(), and run the test cases there to simulate the code"""


#!/usr/bin/env python3
from FourConnect import * # See the FourConnect.py file
import csv
import math
import time


class GameTreePlayer:
    
    def __init__(self):
        pass
        
    def is_valid_move(self, board, col): #check for validity of move
        return 0 <= col < 7 and board[0][col] == 0  # Check if the column is within bounds and not full
    
    def there_is_a_winner(self, board, piece):
        # Check horizontally
        for c in range(4):
            for r in range(6):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True

	# Check vertical locations for win
        for c in range(7):
            for r in range(3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(4):
            for r in range(3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(4):
            for r in range(3, 6):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True
                

     
    def is_board_full (self,state):     #checks if gameboard is full
        for i in range (0,7) :
            if state[0][i] == 0 :
                return False
        return True

    def is_valid_location(self, board, col) :
        return board[0][col] == 0

      """Evaluation Function 1"""
    # def EVALUATE(self, board, player):      
            
    #     return random.randint(0, 1000)

      """Evaluation Function 2
      Utility function already has win utilities assigned to it, so this will only return other terminal states which have utility as 0"""
    # def EVALUATE(self, board, player):      
            
    #     return 0

      """Evaluation Function 3"""
    # def EVALUATE (self,board, player ) :
    #     score=0
    #     for c in range(7):
    #         col_array = [board[0][c],board[1][c],board[2][c],board[3][c],board[4][c],board[5][c]]
    #         score += self._evaluate_window(col_array,player)

    #     ## Score Horizontal
    #     for r in range(6):
    #         row_array = board[r]
    #         score += self._evaluate_window(row_array,player)
    #         if(row_array.count(2)==4 and row_array.count(0)==2):
    #             score+=5
    #     return score
    
    # def _evaluate_window(self,window,player):   #change
    #     score = 0
    #     score = 0
    #     #print(window)
    #     for i in range(len(window)-3):
    #         temp = window[i:i+4]
    #         if(temp.count(player)==4 and temp.count(0)==0 ):
    #             score+=10000
    #         if(temp.count(player)==3 and temp.count(0)==1 ):
    #             score+=36
    #         if(temp.count(player)==2 and temp.count(0)==2 ):
    #             score+=6
    #         if(temp.count(player)==1 and temp.count(0)==3 ):
    #             score+=1
    #     return score


      """Evaluation Function 4"""
    # def EVALUATE(self, board):
    #     util = 0

    #     # Pattern matching
    #     # Higher weights for longer patterns, emphasizing the importance of connecting more pieces
    #     for row in range(6):
    #         for col in range(4):
    #             if all(board[row][col + i] == 2 for i in range(4)):
    #                 util += 5000

    #             # Check diagonally (from bottom-left to top-right)
    #             if all(board[row - i][col + i] == 2 for i in range(4)):
    #                 util += 5000


    #     # Higher weights for patterns closer to completion to prioritize blocking the opponent's potential wins
    #     for row in range(6):
    #         for col in range(4):
    #             if all(board[row][col + i] == 1 for i in range(4)):
    #                 util -= 50000

    #             # Check diagonally (from bottom-left to top-right)
    #             if all(board[row - i][col + i] == 1 for i in range(4)):
    #                 util -= 50000

    #         if all(board[row][col + i] == 1 for i in range(4)):
    #             util -= 50000

    #         # Check diagonally (from bottom-left to top-right)
    #         if all(board[row - i][col + i] == 1 for i in range(4)):
    #             util -= 50000

    #     # Control of important positions
    #     # Prioritize center columns and edges to gain more strategic options and limit the opponent's control
    #     center_columns = [3, 4]
    #     for row in range(6):
    #         for col in center_columns:
    #             if board[row][col] == 2:
    #                 util += 100


    #     # Safety
    #     # Prioritize protecting your pieces from being captured or blocked
    #     for row in range(6):
    #         for col in range(5):
    #             if board[row][col] == 2 and board[row][col + 1] == 0:
    #                 util -= 100

    #     # Closeness to winning
    #     # Encourage focusing on moves that can lead to victory directly
    #     for row in range(6):
    #         for col in range(3):
    #             if board[row][col] == 2 and board[row][col + 1] == 2:
    #                 util += 150

    #     return util


        
    def UTILITY(self, board):
        util = 0
        if self.there_is_a_winner(board, 1) :
            return -10000
        elif self.there_is_a_winner(board, 2) :
            return 10000
        elif self.is_board_full(board) :
            return 0
        else :
            return self.EVALUATE(board, 2) - self.EVALUATE(board, 1)
            




    def result(self, state, action, player):
    

        # Check if the action is valid
        # Drop the current player's coin into the selected column
        for row in range(5,-1,-1):
            if state[row][action] == 0:
                state[row][action] = player  # 2 is the current player's number
                break

        # Return the new state
        return state
    

    def alpha_beta(self, board, max_player, depth,alpha,beta) :
        if depth == 0 or self.there_is_a_winner(board, 1) or self.there_is_a_winner(board, 2) or self.is_board_full(board) :
            # print(self.UTILITY(board))
            # temp = FourConnect()
            # temp.SetCurrentState(board)
            # temp.PrintGameState()
            # time.sleep(2)
            return  None, self.UTILITY(board)
        
        if max_player == 2 :
            value = -math.inf
            column = None
            for col in [3,2,4,1,5,0,6] :
                if self.is_valid_move(board, col) :
                    b_copy = copy.deepcopy(board)
                    self.result(b_copy, col, max_player)
                    temp_col, new_score = self.alpha_beta(b_copy, 1, depth-1,alpha,beta )
                    if new_score > value :
                        value = new_score
                        column = col
                    alpha = max(alpha,new_score)
                    if(alpha>=beta):
                        break
            return column, value
        else :
            value = math.inf
            column = None
            for col in [3,2,4,1,5,0,6] :
                if self.is_valid_move(board, col) :
                    b_copy = copy.deepcopy(board)
                    self.result(b_copy, col, max_player)
                    temp_col, new_score = self.alpha_beta(b_copy, 2, depth-1,alpha,beta )
                    if new_score < value :
                        value = new_score
                        column = col
                    beta = min(beta,new_score)
                    if(alpha>=beta):
                        break
            return column, value


    def minimax (self, board, max_player, depth) :
        if depth == 0 or self.there_is_a_winner(board, 1) or self.there_is_a_winner(board, 2) or self.is_board_full(board) :
            #print(self.UTILITY(board))
            #temp = FourConnect()
            #temp.SetCurrentState(board)
            #temp.PrintGameState()
            ##time.sleep(2)
            return  None, self.UTILITY(board)
        
        if max_player == 2 :
            value = -math.inf
            column = None
            for col in range (7) :
                if self.is_valid_move(board, col) :
                    b_copy = copy.deepcopy(board)
                    self.result(b_copy, col, max_player)
                    temp_col, new_score = self.minimax(b_copy, 1, depth-1 )
                    if new_score > value :
                        value = new_score
                        column = col
            return column, value
        else :
            value = math.inf
            column = None
            for col in range (7) :
                if self.is_valid_move(board, col) :
                    b_copy = copy.deepcopy(board)
                    self.result(b_copy, col, max_player)
                    temp_col, new_score = self.minimax(b_copy, 2, depth-1 )
                    if new_score < value :
                        value = new_score
                        column = col
            return column, value
        
        



        

    
    def FindBestAction(self,currentState):
        """
        Modify this function to search the GameTree instead of getting input from the keyboard.
        The currentState of the game is passed to the function.
        currentState[0][0] refers to the top-left corner position.
        currentState[5][6] refers to the bottom-right corner position.
        Action refers to the column in which you decide to put your coin. The actions (and columns) are numbered from left to right.
        Action 0 is refers to the left-most column and action 6 refers to the right-most column.
        """
        alpha = float('-inf')
        beta = float('inf')
        bestAction,_ = self.alpha_beta(currentState,2,5,alpha,beta)
        return bestAction


def LoadTestcaseStateFromCSVfile():
    testcaseState=list()
    with open('testcase.csv', 'r') as read_obj : 
        csvReader = csv.reader(read_obj)
        for csvRow in csvReader :
            row = [int(r) for r in csvRow]
            testcaseState.append(row)
        return testcaseState



def PlayGame():
    fourConnect = FourConnect()
    fourConnect.PrintGameState()
    gameTree = GameTreePlayer()
    
    move=0
    while move<42: #At most 42 moves are possible
        if move%2 == 0: #Myopic player always moves first
            fourConnect.MyopicPlayerAction()
        else:
            currentState = fourConnect.GetCurrentState()
            gameTreeAction = gameTree.FindBestAction(currentState)
            fourConnect.GameTreePlayerAction(gameTreeAction)
        fourConnect.PrintGameState()
        move += 1
        if fourConnect.winner!=None:
            break
    
    """
    You can add your code here to count the number of wins average number of moves etc.
    You can modify the PlayGame() function to play multiple games if required.
    """
    if fourConnect.winner==None:
        print("Game is drawn.")
    else:
        print("Winner : Player {0}\n".format(fourConnect.winner))
    print("Moves : {0}".format(move))

    

def main():
    
    PlayGame()
    """
    You can modify PlayGame function for writing the report
    Modify the FindBestAction in GameTreePlayer class to implement Game tree search.
    You can add functions to GameTreePlayer class as required.
    """

    """
        The above code (PlayGame()) must be COMMENTED while submitting this program.
        The below code (RunTestCase()) must be UNCOMMENTED while submitting this program.
        Output should be your rollnumber and the bestAction.
        See the code for RunTestCase() to understand what is expected.
    """
    


if __name__=='__main__':
    main()
