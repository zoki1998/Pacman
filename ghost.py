from PyQt5.QtCore import (QRectF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QImage)
from PyQt5.QtWidgets import QGraphicsItem


class Ghost(QGraphicsItem):

    def __init__(self, x = 10, y = 10,
                 colour='green', icon='images/ghost.png'):
        QGraphicsItem.__init__(self)
        self.colour = colour

        self.i = QImage(icon)
        self.way = 0
        self.x = x
        self.y = y

    def paint(self, painter):
        x, y = self.x, self.y
        target = QRectF(x * 42+2, y * 42+2, 38, 38)
        source = QRectF(0, 0, 38, 38)
        painter.drawImage(target, self.i, source)



