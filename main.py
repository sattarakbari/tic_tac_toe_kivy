from kivy.lang import Builder
from kivymd.app import MDApp
import numpy as np



class MainApp(MDApp):
    board = np.empty(9)
    board[:] = np.NAN

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('tic_tac_toe.kv')

    # Define Who's turn it is
    turn = "X"

    def presser(self, btn, index):
        if self.turn == 'X':

            btn.text = "X"
            btn.disabled = True
            self.root.ids.score.text = "O's Turn!"
            self.turn = "O"
        else:
            btn.text = "O"
            btn.disabled = True
            self.root.ids.score.text = "X's Turn!"
            self.turn = "X"
        # update the board
        self.board[index] = 1 if self.turn == 'X' else 0

        # Check To See if won
        self.win()

    def restart(self):
        # Reset Who's Turn It Is
        self.turn = "X"
        self.board = np.zeros(9)-1
        # Enable The Buttons
        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False

        # Clear The Buttons
        self.root.ids.btn1.text = ""
        self.root.ids.btn2.text = ""
        self.root.ids.btn3.text = ""
        self.root.ids.btn4.text = ""
        self.root.ids.btn5.text = ""
        self.root.ids.btn6.text = ""
        self.root.ids.btn7.text = ""
        self.root.ids.btn8.text = ""
        self.root.ids.btn9.text = ""

        # Reset The Score Label
        self.root.ids.score.text = "X GOES FIRST!"

    def hashBoard(self):
        return self.board.reshape([3, 3])

    def win(self):
        win = False
        winner = ''
        boardState = self.hashBoard()

        for i in range(3):

            if np.sum(boardState[i, :] == 0) == 3 or np.sum(boardState[i, :] == 1) == 3:
                win = True
                if self.turn == 'X':
                    winner = 'O'
                else:
                    winner = 'X'
            elif np.sum(boardState[:, i] == 0) == 3 or np.sum(boardState[:, i] == 1) == 3:
                win = True
                if self.turn == 'X':
                    winner = 'O'
                else:
                    winner = 'X'
        print(np.array([boardState[1, 1], boardState[0, 0], boardState[2, 2]]) == 0)
        if np.sum(np.array([boardState[1, 1], boardState[0, 0], boardState[2, 2]]) == 0) == 3 or np.sum(
                np.array([boardState[1, 1], boardState[0, 0], boardState[2, 2]]) == 1) == 3:
            win = True
            if self.turn == 'X':
                winner = 'O'
            else:
                winner = 'X'
        if np.sum(np.array([boardState[2, 0], boardState[1, 1], boardState[0, 2]]) == 0) == 3 or np.sum(
                np.array([boardState[2, 0], boardState[1, 1], boardState[0, 2]]) == 1) == 3:
            win = True
            if self.turn == 'X':
                winner = 'O'
            else:
                winner = 'X'
        if win == True:
            self.root.ids.btn1.disabled = True
            self.root.ids.btn2.disabled = True
            self.root.ids.btn3.disabled = True
            self.root.ids.btn4.disabled = True
            self.root.ids.btn5.disabled = True
            self.root.ids.btn6.disabled = True
            self.root.ids.btn7.disabled = True
            self.root.ids.btn8.disabled = True
            self.root.ids.btn9.disabled = True
            self.root.ids.score.text = '%s is the winner' % winner


MainApp().run()
