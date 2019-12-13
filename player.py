from PyQt5.QtCore import (QRectF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QImage)
from PyQt5.QtWidgets import QGraphicsItem


class Player(QGraphicsItem):

    def __init__(self, x=0, y=10,
                 colour='green', icon='images/pacman.ico'):
        QGraphicsItem.__init__(self)

        self.key = 0
        self.oldkey = 0

        self.pocetak = 0

        self.game_over = False

        self.colour = colour
        self.i = QImage(icon)
        self.i2 = QImage(icon)
        self.i3 = QImage('images/pacman2.png')
        self.img = QImage('images/pacman5.png')
        self.img2 = QImage('images/pacman6.png')


        self.poeni = 0
        self.zivot = 3
        self.x = x
        self.y = y

    def paint(self, painter):
        x, y = self.x, self.y
        target = QRectF(x * 42 + 10, y * 42 + 10, 42, 42)
        source = QRectF(0, 0, 42, 42)
        if self.game_over == False:
            painter.drawImage(target, self.i, source)


def zivot(player):

    if player.zivot > 0:
        player.zivot = player.zivot - 1;
        if player.id == 1:
            player.x = 0
            player.y = 10
            player.i = QImage('images/pacman.ico')
        else:
            player.x = 20
            player.y = 10
            player.i = QImage('images/pacman2.png')

        player.pocetak = 1
    else:
        player.game_over = True


def movePlayer(newX, newY, player, dots, tiles, board):

    x = newX
    y = newY
    if player.game_over == False:
        if x < 0 or x * 42 >= 882 or y < 0 or y * 42 >= 924:
            if x == -1 and y == 10 and player.key == 1:

                x = 20
                y = 10

                player.oldkey = player.key
                player.x = x
                player.y = y

                if dots.tacka[x * 22 + y] != 0:

                    if dots.tacka[x * 22 + y] == 1:
                        player.poeni = player.poeni + 10
                    else:
                        player.poeni = player.poeni + 20
                        board.opcija = True
                        board.broj = board.broj + 5
                        board.brojac1 = 0

                    dots.tacka[x * 22 + y] = 0

                board.levelUp() #provjera da li je usao u portal, ako jeste proveriti da li je pojeo duhove
                return True

            elif x == 21 and y == 10 and player.key == 2:

                x = 0
                y = 10

                player.oldkey = player.key
                player.x = x
                player.y = y

                if dots.tacka[x * 22 + y] != 0:

                    if dots.tacka[x * 22 + y] == 1:
                        player.poeni = player.poeni + 10
                    else:
                        player.poeni = player.poeni + 20
                        board.opcija = True
                        board.broj = board.broj + 5
                        board.brojac1 = 0

                    dots.tacka[x * 22 + y] = 0
                board.levelUp()
                return True

            else:
                player.key = 0
                return False

        if tiles[x * 22 + y] == 10:
            player.key = player.oldkey
            return False

        player.oldkey = player.key
        player.x = x
        player.y = y

        if dots.tacka[x * 22 + y] != 0:

            if dots.tacka[x * 22 + y] == 1:
                player.poeni = player.poeni + 10
            else:
                player.poeni = player.poeni + 20
                board.opcija = True  #BONUS --
                board.broj = board.broj + 5
                board.brojac1 = 0

            dots.tacka[x * 22 + y] = 0
    else:
        player.x = 8
        player.y = 10

    return True
