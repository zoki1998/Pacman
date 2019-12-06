from PyQt5 import QtGui, QtTest
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QGraphicsScene
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QTimer
from PyQt5.QtGui import QPainter, QColor, QTransform, QImage
import sys, time

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

        self.color1 = 0xFF0000
        self.color2 = 0x000000
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
        t = QTransform()
        t.rotate(90)

        if key == Qt.Key_P:
            self.pause()
            return

        elif key == Qt.Key_Left:
            #self.pp.i = self.pp.i2
            self.pp.i.convertToFormat(QImage.Format_RGB888)
            self.pp.i = self.pp.i3
            self.key = 1
            """while (self.tiles[(self.pp.x - 2) * 22 + self.pp.y - 1] != 10 and self.pp.x != 1):
                if (self.tryMove(self.pp, self.pp.x - 1, self.pp.y) == FALSE):
                    break"""
            self.tryMove(self.pp, self.pp.x-1, self.pp.y )


        elif key == Qt.Key_Right:
            self.pp.i = self.pp.i2
            self.key = 2
            """while (self.tiles[self.pp.x * 22 + self.pp.y - 1] != 10 and self.pp.x != 20):
                if (self.tryMove(self.pp, self.pp.x + 1, self.pp.y) == FALSE):
                    break
            if(self.pp.x == 20 and self.pp.y == 11):
                self.tryMove(self.pp, self.pp.x + 1, self.pp.y)"""
            self.tryMove(self.pp, self.pp.x + 1, self.pp.y)

        elif key == Qt.Key_Down:
            self.key = 3
            self.pp.i = self.pp.i2
            self.pp.i.convertToFormat(QImage.Format_RGB888)
            self.pp.i = self.pp.i.transformed(t)
            self.tryMove(self.pp, self.pp.x, self.pp.y + 1)
            """ while (self.tiles[(self.pp.x - 1) * 22 + self.pp.y] != 10):
                if (self.tryMove(self.pp, self.pp.x, self.pp.y + 1) == FALSE):
                    break """


        elif key == Qt.Key_Up:
            self.pp.i = self.pp.i2
            self.key = 4
            self.pp.i.convertToFormat(QImage.Format_RGB888)
            self.pp.i = self.pp.i.transformed(t)
            self.pp.i = self.pp.i.transformed(t)
            self.pp.i = self.pp.i.transformed(t)
            self.tryMove(self.pp, self.pp.x, self.pp.y - 1)
            """
            while (self.tiles[(self.pp.x - 1) * 22 + self.pp.y - 2] != 10):
                if (self.tryMove(self.pp, self.pp.x, self.pp.y - 1) == FALSE):
                    break """

        else:
            super(Board, self).keyPressEvent(event)

    def tryMove(self, new, newX, newY):

        x = newX
        y = newY

        if x < 0 or x*42 >= Board.BoardWidth or y < 0 or y*42 >= Board.BoardHeight:
            if x == -1 and y == 10 and self.key == 1:
                x = 20
                y = 10
                self.pp.x = x
                self.pp.y = y
                self.update()
                return True
            elif x == 21 and y == 10 and self.key == 2:
                x = 0
                y = 10
                self.pp.x = x
                self.pp.y = y
                self.update()
                return True
            else:
                 return False
        if self.tiles[x*22+y] == 10:
            return False


        self.pp.x = x
        self.pp.y = y
        self.update()

        return True

