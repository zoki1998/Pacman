from PyQt5.QtCore import (QRectF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QImage)
from PyQt5.QtWidgets import QGraphicsItem
import random as ran
import player as pl

class Ghost(QGraphicsItem):

    def __init__(self, x=10, y=10, x1=0, y1=0,
                 colour='green', icon='images/ghost.png'):
        QGraphicsItem.__init__(self)
        self.colour = colour
        self.i = QImage(icon)
        self.i2 = QImage("images/scaredghost.png")
        self.way = 0
        self.way1 = 0
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.sakriven = False


    def paint(self, painter,opcija):

        x, y = self.x, self.y
        target = QRectF(x * 42+2 + self.x1, y * 42+2 + self.y1, 38, 38)
        source = QRectF(0, 0, 38, 38)
        if self.sakriven == False:
            if opcija == False:
                painter.drawImage(target, self.i, source)
            else:
                painter.drawImage(target, self.i2, source)


def move(tiles, ghost, player, player1, opcija):

    l = [] #for free positions
    if opcija == False:  #da li je bonus (onda igrac jede duhove)

        if ghost.x*42 + ghost.x1 == player1.x*42 + player1.x1 and ghost.y*42 + ghost.y1 == player1.y*42 + player1.y1:
            pl.zivot(player1)
        if ghost.x*42 + ghost.x1 == player.x*42 + player.x1 and ghost.y*42 + ghost.y1 == player.y*42 + player.y1:
            pl.zivot(player)

    else:
        if ghost.x * 42 + ghost.x1 == player1.x * 42 + player1.x1 and ghost.y * 42 + ghost.y1 == player1.y * 42 + player1.y1:
            ghost.sakriven = True
            player.poeni = player.poeni + 500
        if ghost.x * 42 + ghost.x1 == player.x * 42 + player.x1 and ghost.y * 42 + ghost.y1 == player.y * 42 + player.y1:
            ghost.sakriven = True
            player1.poeni = player1.poeni + 500

    if ghost.sakriven == False:
        if ghost.x + 1 != 21:
            if tiles[(ghost.x + 1) * 22 + ghost.y] != 10:
                if  ghost.way != 3:
                    l.append(4)
        if ghost.x - 1 != -1:
            if tiles[(ghost.x - 1) * 22 + ghost.y] != 10:
                if ghost.way != 4:
                    l.append(3)
        if tiles[ghost.x * 22 + 1 + ghost.y] != 10 and (ghost.x != 10 and ghost.y != 9):
            if ghost.way != 1:
                l.append(2)
        if tiles[ghost.x * 22 - 1 + ghost.y] != 10:
            if ghost.way != 2:
                l.append(1)

        if ghost.way1 == 0:
            if len(l) != 0:
                d = ran.randrange(0, len(l))
                if l[d] == 1:
                    ghost.x = ghost.x
                    ghost.y1 = ghost.y1 - 4.20
                    ghost.way1 = 1

                elif l[d] == 2:
                    ghost.x = ghost.x
                    ghost.y1 = ghost.y1 + 4.20
                    ghost.way1 = 2
                elif l[d] == 3:
                    ghost.x1 = ghost.x1 - 4.20
                    ghost.way1 = 3

                    if ghost.x == -1:
                        ghost.x = 20
                    ghost.y = ghost.y
                elif l[d] == 4:
                    ghost.x1 = ghost.x1 + 4.20
                    ghost.way1 = 4
                    if ghost.x == 21:
                        ghost.x = 0
                    ghost.y = ghost.y

                ghost.way = l[d]

            else:
                if ghost.way == 4:

                    ghost.x1 = ghost.x1 + 4.20
                    ghost.way1 = 4
                    if ghost.x == 21:
                        ghost.x = 0
                    ghost.y = ghost.y

                elif ghost.way == 3:

                    ghost.x1 = ghost.x1 - 4.20
                    ghost.way1 = 3
                    if ghost.x == -1:
                        ghost.x = 20
                    ghost.y = ghost.y

                elif ghost.way == 2:
                    ghost.x = ghost.x
                    ghost.y1 = ghost.y1 + 4.20
                    ghost.way1 = 2

                elif ghost.way == 1:
                    ghost.x = ghost.x
                    ghost.y1 = ghost.y1 - 4.20
                    ghost.way1 = 1
        else:
            if ghost.way1 == 1:
                ghost.x = ghost.x
                ghost.y1 = ghost.y1 - 4.20
                if ghost.y1 <= -42:
                    ghost.y1 = 0
                    ghost.y = ghost.y - 1
                    ghost.way1=0
            elif ghost.way1 == 2:
                ghost.x = ghost.x
                ghost.y1 = ghost.y1 + 4.20
                if ghost.y1 >= 42:
                    ghost.y1 = 0
                    ghost.y = ghost.y + 1
                    ghost.way1 = 0
            elif ghost.way1== 3:
                ghost.x1 = ghost.x1 - 4.20
                if ghost.x1 <= -42:
                    ghost.x1 = 0
                    ghost.x = ghost.x - 1
                    ghost.way1 = 0
                if ghost.x == -1:
                    ghost.x = 20
                ghost.y = ghost.y
            else:
                ghost.x1 = ghost.x1 + 4.20
                if ghost.x1 >= 42:
                    ghost.x1 = 0
                    ghost.x = ghost.x + 1
                    ghost.way1 = 0
                if ghost.x == 21:
                    ghost.x = 0
                ghost.y = ghost.y

    if opcija == False:
        if ghost.x * 42 + ghost.x1 == player1.x * 42 + player1.x1 and ghost.y * 42 + ghost.y1 == player1.y * 42 + player1.y1:
            pl.zivot(player1)
        if ghost.x * 42 + ghost.x1 == player.x * 42 + player.x1 and ghost.y * 42 + ghost.y1 == player.y * 42 + player.y1:
            pl.zivot(player)
    else:

        if ghost.x * 42 + ghost.x1 == player1.x * 42 + player1.x1 and ghost.y * 42 + ghost.y1 == player1.y * 42 + player1.y1:
            ghost.sakriven = True
            player.poeni = player.poeni + 500
        if ghost.x * 42 + ghost.x1 == player.x * 42 + player.x1 and ghost.y * 42 + ghost.y1 == player.y * 42 + player.y1:
            ghost.sakriven = True
            player1.poeni = player1.poeni + 500

    if ghost.sakriven == True:

        ghost.x = 8
        ghost.y = 10



