import numpy


class Player:
    name = ''
    gamesPlayed = 0
    wins = 0


    def __init__(self, name):
        self.name = name
        self.indexesOnCurrentBoard = list()
