import numpy


class Board:
    rows = 3
    cols = 3
    state = ['']*rows*cols

    def getState(self):
        return self.state

    def update(self, index, text):
        self.state[index] = text

    def hashBoard (self):
        pass


