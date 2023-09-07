"""
this class is responsible for storing all he information about the current state of a chess game.
it will also be responsible for detarmining the valid moves at the current state
it will also keep a move log.
"""
class GameState ():
    def __init__ (self):
        #
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        if self.isMoveValid(move):
             self.board[move.startRow][move.startCol], self.board[move.endRow][move.endCol] = self.board[move.endRow][move.endCol], self.board[move.startRow][move.startCol]
             self.moveLog.append(move)
             self.whiteToMove = not self.whiteToMove
             return True
        return False


    def isMoveValid(self, move):
    # Check if the move is within the bounds of the board
        if not (0 <= move.startRow < 8) or not (0 <= move.startCol < 8) or not (0 <= move.endRow < 8) or not (0 <= move.endCol < 8):
             return False

    # Check if the piece at the start position belongs to the current player
        if (self.whiteToMove and not self.board[move.startRow][move.startCol].startswith('w')) or (not self.whiteToMove and not self.board[move.startRow][move.startCol].startswith('b')):
             return False

    # Implement specific logic for the pawn's valid moves here
    # Example: Check if it's a valid pawn move (e.g., forward, capture, en passant, promotion, etc.)

    # Check if the move doesn't put the player's king in check
    # You'll need to implement a separate method to check for this

        return True
  
class Move:
    ranksToRows = {"1": 7,"2": 6,"3": 5,"4":4,"5": 3,"6": 2, "7": 1, "8":0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    fileToCols = {"a": 0,"b": 1,"c": 2,"d": 3,"e": 4,"f": 5,"g": 6,"h": 7}
    colsToFiles = {v: k for k, v in fileToCols.items()} 
    
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        
    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)  # Corrected this line

        
    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
    
    
    
    