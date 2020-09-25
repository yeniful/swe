import sys
import random
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.uic import loadUiType
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt

form_class=loadUiType("Sudoku.ui")[0]

class SudokuUI(QMainWindow, form_class):

    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)

        self.ButtonList = [[self.A00, self.A01, self.A02, self.A03, self.A04, self.A05, self.A06, self.A07, self.A08],
                           [self.A10, self.A11, self.A12, self.A13, self.A14, self.A15, self.A16, self.A17, self.A18],
                           [self.A20, self.A21, self.A22, self.A23, self.A24, self.A25, self.A26, self.A27, self.A28],
                           [self.A30, self.A31, self.A32, self.A33, self.A34, self.A35, self.A36, self.A37, self.A38],
                           [self.A40, self.A41, self.A42, self.A43, self.A44, self.A45, self.A46, self.A47, self.A48],
                           [self.A50, self.A51, self.A52, self.A53, self.A54, self.A55, self.A56, self.A57, self.A58],
                           [self.A60, self.A61, self.A62, self.A63, self.A64, self.A65, self.A66, self.A67, self.A68],
                           [self.A70, self.A71, self.A72, self.A73, self.A74, self.A75, self.A76, self.A77, self.A78],
                           [self.A80, self.A81, self.A82, self.A83, self.A84, self.A85, self.A86, self.A87, self.A88]]

        for i in range(0,9):
            for number in self.ButtonList[i]:
                number.clicked.connect(self.NumClick)

        self.AVal = []

        for i in range(0,9):
            temp = []
            for j in range(0,9):
                temp.append(str(self.ButtonList[i][j].text()))
            self.AVal.append(temp)


        self.ShuffleClick()
        self.ShuffleButton.clicked.connect(self.ShuffleClick)
        self.FinishButton.clicked.connect(self.CompleteTestClick)

    def ShuffleClick(self):
        random19 = list(range(1,10)) # [1,2,3,4,5,6,7,8,9]
        random.shuffle(random19)

        for i in range(0,9):
            for j in range(0,9):
                self.ButtonList[i][j].setText(str(random19[int(self.AVal[i][j])-1]))

        for i in range(0,9):
            for j in range(0,9):
                if random.random() > float(self.pEdit.text()):
                    self.ButtonList[i][j].setText("")

    def NumClick(self):
        pass

    def keyPressEvent(self, event):
        pass


    def CompleteTestClick(self):
        pass

app=QApplication(sys.argv)
myWindow=SudokuUI(None)
myWindow.show()
app.exec_()


