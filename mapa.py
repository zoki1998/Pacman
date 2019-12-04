from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
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
        self.resize(840, 840)

        self.center()
        self.show()

    def center(self):
        """centers the window on the screen"""

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


class Board(QFrame):
    BoardWidth = 800
    BoardHeight = 800

    def __init__(self, parent):
        self.pp = p.Player()
        super().__init__(parent)
        self.resize(800, 800)

        self.tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
            0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.contentsRect( )
        for x in range(20):
            for y in range(20):
                if self.tiles[x * 20 + y] == 0:
                    self.draw(x * 42, y * 42, painter, QColor(0x6666CC))
                else:
                    self.draw(x * 42, y * 42, painter, QColor(0xFF0000))

    def draw(self, x, y, painter, color):
        painter.fillRect(x + 1, y + 1, self.squareHeight() - 2,
                         self.squareWidth() - 2, color)

        # painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareWidth() - 1, x, y)
        painter.drawLine(x, y, x + self.squareHeight() - 1, y)

        #  painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareWidth() - 1,
                         x + self.squareHeight() - 1, y + self.squareWidth() - 1)
        painter.drawLine(x + self.squareHeight() - 1,
                         y + self.squareWidth() - 1, x + self.squareHeight() - 1, y + 1)
        self.pp.paint(painter, self)

    def squareWidth(self):
        return 42

    def squareHeight(self):
        return 42
