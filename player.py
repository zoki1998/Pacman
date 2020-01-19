from PyQt5.QtCore import (QRectF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QImage)
from PyQt5.QtWidgets import QGraphicsItem


class Player(QGraphicsItem):

    def __init__(self, x=0, y=10, x1=0, y1=0,
                 colour='green', icon='images/pacman.ico'):
        QGraphicsItem.__init__(self)

        self.key = 0
        self.oldkey = 0
        self.pom=0

        self.pocetak = 0

        self.game_over = False

        self.colour = colour
        self.i = QImage(icon)
        self.i2 = QImage(icon)
        self.i3 = QImage('images/pacman2.png')
        self.img = QImage('images/pacman5.png')
        self.img2 = QImage('images/pacman6.png')

        self.way1 = 0
        self.poeni = 0
        self.zivot = 3
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.konacno=x,y
    def paint(self, painter):
        x, y = self.x, self.y
        target = QRectF(x * 42 + 10 + self.x1, y * 42 + 10 + self.y1, 42, 42)
        source = QRectF(0, 0, 42, 42)
        if self.game_over == False:
            painter.drawImage(target, self.i, source)


def zivot(player):

    if player.zivot > 0:
        player.zivot = player.zivot - 1;
        player.x1 = 0
        player.y1 = 0
        player.oldkey=0
        player.way1=0
        player.key=0
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


def movePlayer(kljuc, player, dots, tiles, board):
    if player.game_over == False:

        if board.opcija == False:  # da li je bonus (onda igrac jede duhove)
            if board.ghost1.x * 42 + board.ghost1.x1 == player.x * 42 + player.x1 and board.ghost1.y * 42 + board.ghost1.y1 == player.y * 42 + player.y1:
                zivot(player)
            if board.ghost2.x * 42 + board.ghost2.x1 == player.x * 42 + player.x1 and board.ghost2.y * 42 + board.ghost2.y1 == player.y * 42 + player.y1:
                zivot(player)
            if board.ghost3.x * 42 + board.ghost3.x1 == player.x * 42 + player.x1 and board.ghost3.y * 42 + board.ghost3.y1 == player.y * 42 + player.y1:
                zivot(player)
            if board.ghost4.x * 42 + board.ghost4.x1 == player.x * 42 + player.x1 and board.ghost4.y * 42 + board.ghost4.y1 == player.y * 42 + player.y1:
                zivot(player)
        elif board.opcija == True:
            if board.ghost1.x * 42 + board.ghost1.x1 == player.x * 42 + player.x1 and board.ghost1.y * 42 + board.ghost1.y1 == player.y * 42 + player.y1:
                board.ghost1.sakriven = True
            if board.ghost2.x * 42 + board.ghost2.x1 == player.x * 42 + player.x1 and board.ghost2.y * 42 + board.ghost2.y1 == player.y * 42 + player.y1:
                board.ghost2.sakriven = True
            if board.ghost3.x * 42 + board.ghost3.x1 == player.x * 42 + player.x1 and board.ghost3.y * 42 + board.ghost3.y1 == player.y * 42 + player.y1:
                board.ghost3.sakriven = True
            if board.ghost4.x * 42 + board.ghost4.x1 == player.x * 42 + player.x1 and board.ghost4.y * 42 + board.ghost4.y1 == player.y * 42 + player.y1:
                board.ghost4.sakriven = True

        if player.way1 == 0:

            if kljuc == 2:
                if checkout(player, board, tiles,kljuc) == True and proveriskretanje(player,tiles,dots,board):
                    player.way1 = 2
                    player.x1 = round(player.x1 + 4.20,2)
                    player.oldkey = player.key
                    checkdots(dots, player, board)
            elif kljuc == 1:
                if checkout(player, board, tiles,kljuc) == True and proveriskretanje(player,tiles,dots,board):
                    player.way1 = 1
                    player.x1 = round(player.x1 - 4.20,2)
                    player.oldkey = player.key
                    checkdots(dots, player, board)

            elif kljuc == 3:
                if checkout(player, board, tiles,kljuc) == True and proveriskretanje(player,tiles,dots,board):
                   player.way1 = 3
                   player.y1 = round(player.y1 + 4.20,2)
                   player.oldkey = player.key
                   checkdots(dots, player, board)
            elif kljuc == 4:
                if checkout(player, board, tiles,kljuc) == True and proveriskretanje(player,tiles,dots,board):
                    player.way1 = 4
                    player.y1 -= 4.
                    player.oldkey = player.key
                    checkdots(dots, player, board)

        else:
            if player.way1 == 2:
                player.x1 = round(player.x1 + 4.20,2)
                if player.x1 >= 42:
                    player.x1 = 0
                    player.x += 1
                    player.way1 = 0
                    checkout(player,board,tiles,1);


            elif player.way1 == 1:
                player.x1 = round(player.x1 - 4.20,2)
                if player.x1 <= -42:
                    player.x1 = 0
                    player.x -= 1
                    player.way1 = 0
                    checkout(player, board, tiles, 2);

            elif player.way1 == 3:
                player.y1 = round(player.y1 + 4.20,2)
                if player.y1 >= 42:
                    player.y1 = 0
                    player.y += 1
                    player.way1 = 0


            else:
                player.y1 = round(player.y1 - 4.20,2)
                if player.y1 <= -42:
                    player.y1 = 0
                    player.y -= 1
                    player.way1 = 0

    else:
        player.x = 8
        player.y = 10
        player.x1 = 0
        player.y1 = 0

    if board.opcija == False:  #da li je bonus (onda igrac jede duhove)
        if board.ghost1.x * 42 + board.ghost1.x1 == player.x * 42 + player.x1 and board.ghost1.y * 42 + board.ghost1.y1 == player.y * 42 + player.y1:
            zivot(player)
        if board.ghost2.x * 42 + board.ghost2.x1 == player.x * 42 + player.x1 and board.ghost2.y * 42 + board.ghost2.y1 == player.y * 42 + player.y1:
            zivot(player)
        if board.ghost3.x * 42 + board.ghost3.x1 == player.x * 42 + player.x1 and board.ghost3.y * 42 + board.ghost3.y1 == player.y * 42 + player.y1:
            zivot(player)
        if board.ghost4.x * 42 + board.ghost4.x1 == player.x * 42 + player.x1 and board.ghost4.y * 42 + board.ghost4.y1 == player.y * 42 + player.y1:
            zivot(player)
    elif board.opcija == True:
        if board.ghost1.x * 42 + board.ghost1.x1 == player.x * 42 + player.x1 and board.ghost1.y * 42 + board.ghost1.y1 == player.y * 42 + player.y1:
            board.ghost1.sakriven = True
        if board.ghost2.x * 42 + board.ghost2.x1 == player.x * 42 + player.x1 and board.ghost2.y * 42 + board.ghost2.y1 == player.y * 42 + player.y1:
            board.ghost2.sakriven = True
        if board.ghost3.x * 42 + board.ghost3.x1 == player.x * 42 + player.x1 and board.ghost3.y * 42 + board.ghost3.y1 == player.y * 42 + player.y1:
            board.ghost3.sakriven = True
        if board.ghost4.x * 42 + board.ghost4.x1 == player.x * 42 + player.x1 and board.ghost4.y * 42 + board.ghost4.y1 == player.y * 42 + player.y1:
            board.ghost4.sakriven = True

def checkdots(dots, player, board):
    if not((player.x == 21 and player.y == 10) or (player.x == -1 and player.y == 10)):
        if dots.tacka[player.x * 22 + player.y] != 0:
            if dots.tacka[player.x * 22 + player.y] == 1:
                player.poeni = player.poeni + 10
            else:
                player.poeni = player.poeni + 200
                board.opcija = True  # BONUS --
                board.broj = board.broj + 5
                board.brojac5 = 0
            dots.tacka[player.x * 22 + player.y] = 0


def checkout(player, board, tiles,kljuc):
    if player.x == -1 and player.y == 10 and kljuc == 1:
        x = 20
        y = 10
        player.oldkey = player.key
        player.x = x
        player.y = y
        player.x1 = 0
        player.y1 = 0
        player.way1 = 0
        board.levelUp()  # provjera da li je usao u portal, ako jeste proveriti da li je pojeo duhove
        return True
    elif player.x == 21 and player.y == 10 and kljuc == 2:
        x = 0
        y = 10
        player.oldkey = player.key
        player.x = x
        player.y = y
        player.x1 = 0
        player.y1 = 0
        player.way1 = 0
        board.levelUp( )
        return True

    return proveriZid(player, tiles,kljuc)


def proveriZid(player,tiles,kljuc):
    if kljuc == 2:
        if (player.x +1 == 21 or player.x+1==22)and player.y == 10:

            return True
        else:
            if tiles[(player.x +1)* 22 + player.y] == 10:
                player.key = player.oldkey
                return False
    elif kljuc == 1:
        if tiles[(player.x -1)* 22 + player.y] == 10:
            player.key = player.oldkey
            return False
    elif kljuc== 3:
        if tiles[player.x * 22 + player.y +1] == 10 or (player.x == 10 and player.y + 1 == 9):
            player.key = player.oldkey
            return False
    elif kljuc == 4:
        if tiles[player.x * 22 + player.y-1] == 10:
            player.key = player.oldkey
            return False
    return True

def proveriskretanje(player,tiles,dots,board):

    if player.pom!=0:
        if player.pom==1:
            if proveriZid(player,tiles,1):
                if checkout(player, board, tiles,1):
                    player.way1 = 1
                    player.x1 = round(player.x1 - 4.20,2)
                    player.oldkey = 1
                    player.key = 1
                    checkdots(dots, player, board)
                    return False
        elif player.pom == 2:
            if proveriZid(player, tiles, 2):
                if checkout(player, board, tiles, 2):
                    player.way1 = 2
                    player.x1 = round(player.x1 + 4.20,2)
                    player.oldkey = 2
                    player.key = 2
                    checkdots(dots, player, board)
                    return False

        elif player.pom == 3:
            if proveriZid(player, tiles, 3):
                if checkout(player, board, tiles, 3):
                    player.way1 = 3
                    player.y1 = round(player.y1 + 4.20,2)
                    player.oldkey = 3
                    player.key = 3
                    checkdots(dots, player, board)
                    return False

        elif player.pom == 4:
            if proveriZid(player, tiles, 4):
                if checkout(player, board, tiles, 4):
                    player.way1 = 4
                    player.y1 = round(player.y1 - 4.20,2)
                    player.oldkey = 4
                    player.key = 4
                    checkdots(dots, player, board)
                    return False
    else:
        return True;