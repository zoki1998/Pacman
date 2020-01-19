from PyQt5.QtCore import (QRectF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QImage)
from PyQt5.QtWidgets import QGraphicsItem
import random as ran

class Force(QGraphicsItem):

    def __init__(self, x=0, y=0,
                 colour='green', icon='images/rotten.png'):
        QGraphicsItem.__init__(self)
        self.colour = colour
        self.i = QImage(icon)
        self.i2 = QImage("images/heart.png")
        self.x = 0
        self.y = 0
        self.option = -1
        self.avaible = []

    def findAvaiblePlaces(self, dots):
        self.avaible.clear()
        for x in range(21):
            for y in range(22):
                if dots.tacka[x*22 +y] == 0 and dots.tacka_pom[x*22 + y] == 1:
                    self.avaible.append((x,y))

    def paint(self, painter):

        target = QRectF(self.x * 42 + 10, self.y * 42 + 10, 25, 25)
        source = QRectF(0, 0, 42, 42)

        if self.x != 0 and self.y != 0:
            if self.option == 0:
                painter.drawImage(target, self.i, source)
            elif self.option == 1:
                painter.drawImage(target, self.i2, source)

    def forceFunction(self, dots, board):

        self.findAvaiblePlaces(dots)

        d = ran.randrange(0, 2)

        self.option = d

        if len(self.avaible) == 0:
            board.prikazanaSila = False
            board.brojacZaSilu = 0
        else:
            k = ran.randrange(0,len(self.avaible))
            self.x,self.y = self.avaible[k]


