from PyQt5.QtCore import (QRectF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QImage)
from PyQt5.QtWidgets import QGraphicsItem


class Player(QGraphicsItem):

    def __init__(self, x = 0, y = 10,
                 colour='green', icon='images/pacman.ico'):
        QGraphicsItem.__init__(self)
        self.id = 1
        self.key =0
        self.oldkey = 0
        self.colour = colour
        self.pocetak = 0
        self.i = QImage(icon)
        self.i2 = QImage(icon)
        self.i3 = QImage('images/pacman2.png')
        self.img = QImage('images/pacman5.png')
        self.img2 = QImage('images/pacman6.png')
        self.poeni = 0
        self.zivot=3
        self.x = x
        self.y = y

    def paint(self, painter):
        x, y = self.x, self.y
        target = QRectF(x * 42 + 10, y * 42 + 10, 42, 42)
        source = QRectF(0, 0, 42, 42)
        painter.drawImage(target, self.i, source)

def zivot(player):

    player.zivot = player.zivot - 1;

    if player.zivot >= 0:
        player.x = 0
        player.y = 10
        player.pocetak = 1
        player.i = QImage('images/pacman.ico')
    #else-gameover



