import numpy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.button import Button
import board

import player


def setButtonText(btn, text: str):
    btn.text = text


def disableButton(btn: Button):
    btn.disabled = True


def enableButton(btn: Button):
    btn.disabled = True


class OnlyThreeApp(MDApp):
    playerX: player.Player
    playerO: player.Player

    def __init__(self, playerX, playerO, board, **kwargs):
        super().__init__(**kwargs)
        self.board = board.Board()
        self.playerO = playerO
        self.playerX = playerX
        self.turn = playerX

    def changeTurn(self):
        self.turn = playerX if self.turn == playerO else playerO

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('tic_tac_toe.kv')

    def getButtons(self):
        return [self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3, self.root.ids.btn4, self.root.ids.btn5,
                self.root.ids.btn6,
                self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9]

    def presser(self, btn, index):
        p: player.Player
        p = self.turn

        # if less than 3 X's or O's ->  set text and disable the button
        if len(p.indexesOnCurrentBoard) < 3:
            p.indexesOnCurrentBoard.append(index)
            btn.disabled = True
            btn.text = p.name

            if len(playerX.indexesOnCurrentBoard) == 3 and len(playerO.indexesOnCurrentBoard) == 3:
                for b in self.getButtons():
                    if b.text != p.name and b.text != '':
                        b.disabled = False
                    else:
                        b.disabled = True

        else:
            p.indexesOnCurrentBoard.remove(index)
            btn.text = ''
            for b in self.getButtons():
                if b.text == '':
                    b.disabled = False
                if b.text == p.name:
                    b.disabled = True
            btn.disabled = True

            self.changeTurn()
        if len(p.indexesOnCurrentBoard) == 3:
            # Check To See if won
            self.win()
        self.changeTurn()

    def restart(self):
        # Reset Who's Turn It Is
        self.turn = playerX

        # Enable The Buttons

        # Clear The Buttons
        for b in self.getButtons():
            b.disabled = False
            b.text = ''

        # Reset othe values
        playerX.indexesOnCurrentBoard = list()
        playerO.indexesOnCurrentBoard = list()

    def win(self):
        win = False
        # check if the current player wins the round
        p: player.Player
        p = self.turn

        indexes =sorted(p.indexesOnCurrentBoard)
        temp_hor = list()
        temp_vert = list()

        for ind in indexes:
            temp_vert.append(numpy.round(ind / 3))
            temp_hor.append(ind % 3)
        if temp_hor[1] == temp_hor[2] and temp_hor[2] == temp_hor[0]:
            win = True
        if temp_vert[1] == temp_vert[2] and temp_vert[2] == temp_vert[0]:
            win = True
        if indexes == [0, 4, 8] or indexes == [2, 4, 6]:
            win = True

        if win == True:
            # disable all the buttons
            for b in self.getButtons():
                b.disabled = True
            # Display the winner
            self.root.ids.t1.text = '%s is the winner' % p.name
            p.wins += 1
            self.root.ids.score.text = '%d:%d' % (playerX.wins, playerO.wins)


playerX = player.Player('X')
playerO = player.Player('O')
app = OnlyThreeApp(playerX, playerO, board)
app.run()
