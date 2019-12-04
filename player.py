import biblioteke as bi
import mapa as m
from PyQt5.QtCore import (QRectF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QImage)
from PyQt5.QtWidgets import QGraphicsItem


class Player(QGraphicsItem):

    def __init__(self, xy=(5, 5),
                 colour='green', icon='images/pacman.ico'):
        QGraphicsItem.__init__(self)
        self.colour = colour
        self.icon = icon
        self.xy = xy

    def paint(self, painter, widget):
        x, y = self.xy
        target = QRectF(x * 30, y * 30, 28, 28)
        source = QRectF(0, 0, 28, 28)
        painter.drawImage(target, QImage(self.icon), source)




"""   def tryMove(self, pl, newX, newY):
        tries to move a shape
            x1=pl.xy[0]
            x2=pl.xy[1]
            x = newX + x1
            y = newY - y1

            if x < 0 or x >= .BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False




        self.xy = x, y
        self.update()

        return True



"""