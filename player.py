import biblioteke as bi
import mapa as m
from PyQt5.QtCore import (QRectF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QImage)
from PyQt5.QtWidgets import QGraphicsItem


class Player(QGraphicsItem):

    def __init__(self, x=0, y=10,
                 colour='green', icon='images/pacman.ico'):
        QGraphicsItem.__init__(self)
        self.colour = colour
        self.i = QImage(icon)
        self.i2 = QImage(icon)
        self.i3 = QImage('images/pacman2.png')
        self.x = x
        self.y = y;

    def paint(self, painter):
        x, y = self.x, self.y
        target = QRectF(x * 42+10, y * 42+10, 42, 42)
        source = QRectF(0, 0, 42, 42)
        painter.drawImage(target, self.i, source)


