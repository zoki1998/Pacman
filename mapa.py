from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QGraphicsScene
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QTimer
from PyQt5.QtGui import QPainter, QColor
import sys
import player as p
from tkinter import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.tboard = Board(self)

        self.initUI( )

    def initUI(self):
        self.setWindowTitle('Pacman')

        self.setCentralWidget(self.tboard)
        self.setWindowIcon(QtGui.QIcon('pacman.ico'))
        self.resize(882, 924)

        self.center()
        self.show()

    def center(self):
        """centers the window on the screen"""

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2-40)


class Board(QFrame):
    BoardWidth = 882
    BoardHeight = 924

    def __init__(self, parent):
        self.pp = p.Player()
        super().__init__(parent)
        self.resize(882, 924)
        self.shape = 10

        self.key = None
        self.setFocusPolicy(Qt.StrongFocus)


        self.timer_interval = 350
        self.scene = QGraphicsScene()
        self.scene.addItem(self.pp)
        self.timer = QTimer(self)

        self.tiles = [
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1,  10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
            10, 3,  12, 12, 9,  12, 5,  10, 10, 10, 1,  10, 10, 10, 3,  12, 5,  10, 3,  12, 5, 10,
            10, 1,  10, 10, 1,  10, 1,  10, 10, 10, 1,  10, 10, 10, 1,  10, 2,  12, 8,  10, 1, 10,
            10, 1,  10, 10, 1,  10, 1,  10, 10, 10, 1,  10, 10, 10, 1,  10, 10, 10, 1,  10, 1, 10,
            10, 6,  12, 12, 11, 12, 7,  12, 12, 12, 11, 12, 12, 12, 11, 12, 9,  12, 4,  10, 1, 10,
            10, 1,  10, 10, 1,  10, 10, 10, 10, 10, 1,  10, 10, 10, 1,  10, 1,  10, 10, 10, 1, 10,
            10, 1,  10, 10, 6,  12, 5,  10, 3,  12, 7,  12, 9,  12, 8,  10, 6,  12, 5,  10, 1, 10,
            10, 1,  10, 10, 1,  10, 1,  10, 1,  10, 10, 10, 1,  10, 1,  10, 1,  10, 1,  10, 1, 10,
            10, 2,  12, 12, 8,  10, 1,  10, 1,  10, 14, 10, 1,  10, 1,  10, 1,  10, 1,  10, 1, 10,
            10, 10, 10, 10, 1,  10, 2,  12, 8,  10, 1,  10, 1,  10, 2,  12, 8,  10, 2,  12, 8, 10,
            10, 10, 10, 10, 1,  10, 10, 10, 6,  12, 8,  10, 1,  10, 10, 10, 1,  10, 10, 10, 1, 10,
            10, 10, 10, 10, 1,  10, 3,  12, 8,  10, 1,  10, 1,  10, 3,  12, 8,  10, 3,  12, 8, 10,
            10, 3,  12, 12, 8,  10, 1,  10, 1,  10, 13, 10, 1,  10, 1,  10, 1,  10, 1,  10, 1, 10,
            10, 1,  10, 10, 1,  10, 1,  10, 1,  10, 10, 10, 1,  10, 1,  10, 1,  10, 1,  10, 1, 10,
            10, 1,  10, 10, 6,  12, 4,  10, 2,  12, 9,  12, 7,  12, 8,  10, 6,  12, 4,  10, 1, 10,
            10, 1,  10, 10, 1,  10, 10, 10, 10, 10, 1,  10, 10, 10, 1,  10, 1,  10, 10, 10, 1, 10,
            10, 6,  12, 12, 11, 12, 9,  12, 12, 12, 11, 12, 12, 12, 11, 12, 7,  12, 5,  10, 1, 10,
            10, 1,  10, 10, 1,  10, 1,  10, 10, 10, 1,  10, 10, 10, 1,  10, 10, 10, 1,  10, 1, 10,
            10, 1,  10, 10, 1,  10, 1,  10, 10, 10, 1,  10, 10, 10, 1,  10, 3,  12, 8,  10, 1, 10,
            10, 2,  12, 12, 7,  12, 4,  10, 10, 10, 1,  10, 10, 10, 2,  12, 4,  10, 2,  12, 4, 10,
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1,  10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
        ]

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.contentsRect( )
        for x in range(21):
            for y in range(22):
                self.setshape(self.tiles[x * 22 + y])
                if self.tiles[x * 22 + y] == 10:
                    self.draw(x * 42, y * 42, painter, QColor(0x000000))
                else:
                    self.draw(x * 42, y * 42, painter, QColor(0x000000))

    def setshape(self,oblik):
        self.shape = oblik


    def draw(self, x, y, painter, color):
        painter.fillRect(x + 1, y + 1, self.squareHeight(),
                         self.squareWidth(), color)

        painter.setPen(QColor(0x000099))

        if self.shape == 3 or self.shape == 5 or self.shape == 9 or self.shape == 12 or self.shape == 14:
            painter.drawLine(x, y + self.squareWidth(), x, y)
            #gore
        if self.shape == 2 or self.shape == 1 or self.shape == 3 or self.shape == 6 or self.shape == 13 or self.shape == 14:
            painter.drawLine(x, y, x + self.squareHeight() - 1, y)

        #  painter.setPen(color.darker())
        #desna

        if self.shape == 1 or self.shape == 4 or self.shape == 5 or self.shape == 8 or self.shape == 13 or self.shape == 14:
            painter.drawLine(x + 1, y + self.squareWidth(),
                         x + self.squareHeight()+1, y + self.squareWidth())
        #donja
        if self.shape == 2 or self.shape == 4 or self.shape == 7 or self.shape == 12 or self.shape == 13:
            painter.drawLine(x + self.squareHeight()+1,
                         y + self.squareWidth() , x + self.squareHeight(), y )
        self.pp.paint(painter)




    def squareWidth(self):
        return 42

    def squareHeight(self):
        return 42

    def timerEvent(self, event):

        super(Board, self).timerEvent(event)

    def keyPressEvent(self, event):
        """processes key press events"""

        key = event.key()

        if key == Qt.Key_P:
            self.pause()
            return

        elif key == Qt.Key_Left:
            self.tryMove(self.pp, self.pp.x - 1, self.pp.y)

        elif key == Qt.Key_Right:
            self.tryMove(self.pp, self.pp.x + 1, self.pp.y)

        elif key == Qt.Key_Down:
            self.tryMove(self.pp, self.pp.x, self.pp.y + 1)

        elif key == Qt.Key_Up:
            self.tryMove(self.pp, self.pp.x, self.pp.y - 1)

        elif key == Qt.Key_Space:
            self.dropDown()

        elif key == Qt.Key_D:
            self.oneLineDown()

        else:
            super(Board, self).keyPressEvent(event)

    def tryMove(self, newPiece, newX, newY):
        """tries to move a shape"""

        x = newX
        y = newY

        if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
            return False

        self.pp.x=x
        self.pp.y=y
        self.update()

        return True

