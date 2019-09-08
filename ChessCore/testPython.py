
"""
This was written by a cool guy named Jose Gamboa
"""

import chess.pgn
import csv

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

    def createCSV(self):
        with open('/Users/josegamboa/Documents/GitHub/ChessAnalytics/ChessCore/data/MyChessDB.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(["Event","Date","White","Black","Result","BlackElo","WhiteElo","ECO"])
            for game in self.games:
                if game != None:
                    csvData = [
                        game.headers["Event"], 
                        game.headers["Date"],
                        game.headers["White"],
                        game.headers["Black"],
                        game.headers["Result"],
                        game.headers["BlackElo"],
                        game.headers["WhiteElo"],
                        game.headers["ECO"]]

                filewriter.writerow(csvData)

#miner = ChessMiner("/data/pgn/pablo.pgn")
miner = ChessMiner("/Users/josegamboa/Documents/GitHub/ChessAnalytics/ChessCore/data/pgn/pablo.pgn")
miner.loadGames()
miner.createCSV()