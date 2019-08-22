
#This is a comment.
"""
This is a comment
written in
more than just one line
"""

import chess.pgn

class ChessMiner:
    def __init__(self, fileName):
        self.fileName = fileName
        self.games = []

    def loadGames(self):
        FILE_NAME = open(self.fileName)
        newGame = chess.pgn.read_game(FILE_NAME)
        self.games.append(newGame)
        while (newGame is not None):
            newGame = chess.pgn.read_game(FILE_NAME)
            self.games.append(newGame)
        return self.games

    def getGames(self):
        if len(self.games) == 0:
            return self.loadGames()
        else:
            return self.games



#miner = ChessMiner("data/pgn/anastasian-lewis.pgn")
miner = ChessMiner("data/pgn/pablo.pgn")
#miner = ChessMiner("data/pgn/kasparov-deep-blue-1997.pgn")

miner.loadGames()

print(len(miner.games))
print("hola")