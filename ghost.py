from PyQt5.QtCore import (QRectF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QImage)
from PyQt5.QtWidgets import QGraphicsItem
import random as ran
import player as pl

class Ghost(QGraphicsItem):

    def __init__(self, x=10, y=10,
                 colour='green', icon='images/ghost.png'):
        QGraphicsItem.__init__(self)
        self.colour = colour
        self.i = QImage(icon)
        self.i2 = QImage("images/scaredghost.png")
        self.way = 0
        self.x = x
        self.y = y
        self.sakriven = False


    def paint(self, painter,opcija):

        x, y = self.x, self.y
        target = QRectF(x * 42+2, y * 42+2, 38, 38)
        source = QRectF(0, 0, 38, 38)
        if self.sakriven == False:
            if opcija == False:
                painter.drawImage(target, self.i, source)
            else:
                painter.drawImage(target, self.i2, source)



def move(tiles, ghost, player, player1, opcija):

    l = [] #for free positions
    if opcija == False:  #da li je bonus (onda igrac jede duhove)
        if ghost.x == player.x and ghost.y == player.y:
            pl.zivot(player)
        if ghost.x == player1.x and ghost.y == player1.y:
            pl.zivot(player1)
    else:
        if ghost.x == player.x and ghost.y == player.y:
            ghost.sakriven = True
        if ghost.x == player1.x and ghost.y == player1.y:
            ghost.sakriven = True

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

        if len(l) != 0:
            d = ran.randrange(0, len(l))
            if l[d] == 1:
                ghost.x = ghost.x
                ghost.y = ghost.y - 1
            elif l[d] == 2:
                ghost.x = ghost.x
                ghost.y = ghost.y + 1
            elif l[d] == 3:
                ghost.x = ghost.x - 1
                if ghost.x == -1:
                    ghost.x = 20
                ghost.y = ghost.y
            elif l[d] == 4:
                ghost.x = ghost.x + 1
                if ghost.x == 21:
                    ghost.x = 0
                ghost.y = ghost.y

            ghost.way = l[d]

        else:
            if ghost.way == 4:
                ghost.x = ghost.x + 1
                if ghost.x == 21:
                    ghost.x = 0
                ghost.y = ghost.y

            elif ghost.way == 3:
                ghost.x = ghost.x - 1
                if ghost.x == -1:
                    ghost.x = 20
                ghost.y = ghost.y

            elif ghost.way == 2:
                ghost.x = ghost.x
                ghost.y = ghost.y + 1

            elif ghost.way == 1:
                ghost.x = ghost.x
                ghost.y = ghost.y - 1

    if opcija == False:
        if ghost.x == player.x and ghost.y == player.y:
            pl.zivot(player)
        if ghost.x == player1.x and ghost.y == player1.y:
            pl.zivot(player1)
    else:
        if ghost.x == player.x and ghost.y == player.y:
            ghost.sakriven = True
            player.poeni=player.poeni+500
        if ghost.x == player1.x and ghost.y == player1.y:
            ghost.sakriven = True
            player1.poeni=player1.poeni+500

    if ghost.sakriven == True:

        ghost.x = 8
        ghost.y = 10



