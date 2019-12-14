from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsScene,QLabel, QApplication, QScrollArea

from PyQt5.QtGui import QTransform, QImage
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QGraphicsView, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, pyqtSlot

from PyQt5.QtGui import QPainter, QColor
import sys, time
import dots as dot

import player as p
import ghost as g


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.startGame()
        self.tboard = Board(self)

        self.initUI( )

    def initUI(self):

        self.setWindowTitle('Pacman-press esc to exit')
        self.setCentralWidget(self.tboard)
        self.setWindowIcon(QtGui.QIcon('pacman.ico'))

        self.resize(882, 964)

        self.tboard.timer.start(self.tboard.timer_interval, self.tboard)

        self.center()
        self.show()

    def startGame(self):
        msgBox = QMessageBox()

        msgBox.setWindowIcon(QtGui.QIcon('pacman.ico'))
        msgBox.setWindowTitle("game")

        msgBox.setText('PACMAN \nStart game')

        msgBox.setStandardButtons(QMessageBox.Yes)

        msgBox.exec()

    def center(self):
        """centers the window on the screen"""

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2-45)


class Board(QFrame):

    BoardWidth = 882
    BoardHeight = 924

    def __init__(self, parent):

        self.pobjednik = 0

        self.player1 = p.Player()
        self.player1.id = 1
        self.player2 = p.Player(20,10)
        self.player2.id = 2
        self.player2.i = self.player2.i3
        self.opcija = False  #za bonus


        self.ghost1 = g.Ghost(8,10)
        self.ghost2 = g.Ghost(9,10)
        self.ghost3 = g.Ghost(11,10)
        self.ghost4 = g.Ghost(12,10)

        self.tt = 0

        self.level = 1

        self.broj = 10 #za timer
        self.pauza = False #p
        self.brojac1 = 0 #za uskoravanje duhova

        super().__init__(parent)

        self.resize(882, 924)
        self.shape = 10
        self.dots = dot.Tacke()

        self.slika_pom = 1 # za mijenjanje slike

        text1 = "Poeni(1): 0    Zivot(1) : 3"
        self.label1 = QLabel(text1, self)
        self.label1.setFont(QtGui.QFont('SansSerif', 15))
        self.label1.move(10, 930)

        text2 = "Poeni(2): 0    Zivot(2) : 3"
        self.label2 = QLabel(text2, self)
        self.label2.setFont(QtGui.QFont('SansSerif', 15))
        self.label2.move(600, 930)

        text3 = "Level: 1"
        self.label3 = QLabel(text3, self)
        self.label3.setFont(QtGui.QFont('SansSerif', 15))
        self.label3.move(400, 930)

        self.brojac = 0 #za timer

        self.player1.key = 0
        self.player1.oldkey = 0
        self.setFocusPolicy(Qt.StrongFocus)

        self.color1 = 0xFF0000
        self.color2 = 0x000000
        self.timer_interval = 20
        self.scene = QGraphicsScene()
        self.scene.addItem(self.player1)
        self.scene.addItem(self.player2)

        self.timer = QBasicTimer()
        self.tiles = [
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1,  10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
            10, 3,  12, 12, 9,  12, 5,  10, 10, 10, 1,  10, 10, 10, 3,  12, 5,  10, 3,  12, 5, 10,
            10, 1,  10, 10, 1,  10, 1,  10, 10, 10, 1,  10, 10, 10, 1,  10, 2,  12, 8,  10, 1, 10,
            10, 1,  10, 10, 1,  10, 1,  10, 10, 10, 1,  10, 10, 10, 1,  10, 10, 10, 1,  10, 1, 10,
            10, 6,  12, 12, 11, 12, 7,  12, 12, 12, 11, 12, 12, 12, 11, 12, 9,  12, 4,  10, 1, 10,
            10, 1,  10, 10, 1,  10, 10, 10, 10, 10, 1,  10, 10, 10, 1,  10, 1,  10, 10, 10, 1, 10,
            10, 1,  10, 10, 6,  12, 5,  10, 3,  12, 7,  12, 9,  12, 8,  10, 6,  12, 5,  10, 1, 10,
            10, 1,  10, 10, 1,  10, 1,  10, 1,  10, 10, 10, 1,  10, 1,  10, 1,  10, 1,  10, 1, 10,
            10, 2,  12, 12, 8,  10, 1,  10, 1,  10, 14, 10, 1,  10, 1,  10, 1,  10, 1,  10, 1, 10,
            10, 10, 10, 10, 1,  10, 2,  12, 8,  10, 1,  10, 1,  10, 2,  12, 8,  10, 2,  12, 8, 10,
            10, 10, 10, 10, 1,  10, 10, 10, 6,  12, 8,  10, 1,  10, 10, 10, 1,  10, 10, 10, 1, 10,
            10, 10, 10, 10, 1,  10, 3,  12, 8,  10, 1,  10, 1,  10, 3,  12, 8,  10, 3,  12, 8, 10,
            10, 3,  12, 12, 8,  10, 1,  10, 1,  10, 13, 10, 1,  10, 1,  10, 1,  10, 1,  10, 1, 10,
            10, 1,  10, 10, 1,  10, 1,  10, 1,  10, 10, 10, 1,  10, 1,  10, 1,  10, 1,  10, 1, 10,
            10, 1,  10, 10, 6,  12, 4,  10, 2,  12, 9,  12, 7,  12, 8,  10, 6,  12, 4,  10, 1, 10,
            10, 1,  10, 10, 1,  10, 10, 10, 10, 10, 1,  10, 10, 10, 1,  10, 1,  10, 10, 10, 1, 10,
            10, 6,  12, 12, 11, 12, 9,  12, 12, 12, 11, 12, 12, 12, 11, 12, 7,  12, 5,  10, 1, 10,
            10, 1,  10, 10, 1,  10, 1,  10, 10, 10, 1,  10, 10, 10, 1,  10, 10, 10, 1,  10, 1, 10,
            10, 1,  10, 10, 1,  10, 1,  10, 10, 10, 1,  10, 10, 10, 1,  10, 3,  12, 8,  10, 1, 10,
            10, 2,  12, 12, 7,  12, 4,  10, 10, 10, 1,  10, 10, 10, 2,  12, 4,  10, 2,  12, 4, 10,
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1,  10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
        ]

    def paintEvent(self, event):

        painter = QPainter(self)
        for x in range(21):
            for y in range(22):
                self.setshape(self.tiles[x * 22 + y])
                self.draw(x * 42, y * 42, painter, QColor(0x000000))
                self.dots.paint(painter, x, y)

        self.player1.paint(painter)
        self.player2.paint(painter)

        self.ghost1.paint(painter,self.opcija)
        self.ghost2.paint(painter,self.opcija)
        self.ghost3.paint(painter,self.opcija)
        self.ghost4.paint(painter,self.opcija)

    def setshape(self, oblik):

        self.shape = oblik

    def draw(self, x, y, painter, color):

        painter.fillRect(x + 1, y + 1, self.squareHeight(),
                         self.squareWidth(), color)

        painter.setPen(QColor(0x000099))

        if self.shape == 3 or self.shape == 5 or self.shape == 9 or self.shape == 12 or self.shape == 14:
            painter.drawLine(x, y + self.squareWidth(), x, y)

            #gore

        if self.shape == 2 or self.shape == 1 or self.shape == 3 or self.shape == 6 or self.shape == 13 or self.shape == 14:
            painter.drawLine(x, y, x + self.squareHeight() - 1, y)

            #desna

        if self.shape == 1 or self.shape == 4 or self.shape == 5 or self.shape == 8 or self.shape == 13 or self.shape == 14:
            painter.drawLine(x + 1, y + self.squareWidth(),
                         x + self.squareHeight()+1, y + self.squareWidth())

             #donja

        if self.shape == 2 or self.shape == 4 or self.shape == 7 or self.shape == 12 or self.shape == 13:
            painter.drawLine(x + self.squareHeight()+1,
                         y + self.squareWidth(), x + self.squareHeight(), y)



    def squareWidth(self):

        return 42

    def squareHeight(self):

        return 42

    def timerEvent(self, event):

        self.checkGameOver()

        t = QTransform()
        t1 = QTransform()
        if(self.brojac % 10) == 0:

            if self.player1.key != 0:

                if self.player1.key == 1:
                    if self.slika_pom == 1:
                        self.player1.i = self.player1.i3
                    else:
                        self.player1.i = self.player1.img2
                    self.tryMove(self.player1.x - 1, self.player1.y,self.player1)

                elif self.player1.key == 2:
                    if self.slika_pom == 1:
                        self.player1.i = self.player1.i2
                    else:
                        self.player1.i = self.player1.img
                    self.tryMove(self.player1.x + 1, self.player1.y,self.player1)

                elif self.player1.key == 3:
                    self.player1.i = self.player1.i2
                    self.player1.i.convertToFormat(QImage.Format_RGB888)
                    t.rotate(90)

                    if self.slika_pom == 1:
                        self.player1.i = self.player1.i.transformed(t)

                    else:
                        self.player1.i = self.player1.img.transformed(t)
                    self.tryMove(self.player1.x, self.player1.y + 1,self.player1)

                elif self.player1.key == 4:
                    self.player1.i = self.player1.i2
                    self.player1.i.convertToFormat(QImage.Format_RGB888)
                    t.rotate(-90)

                    if self.slika_pom == 1:
                        self.player1.i = self.player1.i.transformed(t)
                    else:
                        self.player1.i = self.player1.img.transformed(t)
                    self.tryMove(self.player1.x, self.player1.y - 1,self.player1)

            if self.player2.key != 0:

                if self.player2.key == 1:

                    if self.slika_pom == 1:
                        self.player2.i = self.player2.i3
                    else:
                        self.player2.i = self.player2.img2
                    self.tryMove(self.player2.x - 1, self.player2.y,self.player2)

                elif self.player2.key == 2:

                    if self.slika_pom == 1:
                        self.player2.i = self.player2.i2
                    else:
                        self.player2.i = self.player2.img
                    self.tryMove(self.player2.x + 1, self.player2.y,self.player2)

                elif self.player2.key == 3:

                    self.player2.i = self.player2.i2
                    self.player2.i.convertToFormat(QImage.Format_RGB888)
                    t1.rotate(90)

                    if self.slika_pom == 1:
                        self.player2.i = self.player2.i.transformed(t1)
                    else:
                        self.player2.i = self.player2.img.transformed(t1)
                    self.tryMove(self.player2.x, self.player2.y + 1,self.player2)

                elif self.player2.key == 4:

                    self.player2.i = self.player2.i2
                    self.player2.i.convertToFormat(QImage.Format_RGB888)
                    t1.rotate(-90)

                    if self.slika_pom == 1:
                        self.player2.i = self.player2.i.transformed(t1)
                    else:
                        self.player2.i = self.player2.img.transformed(t1)
                    self.tryMove(self.player2.x, self.player2.y - 1,self.player2)

            if self.slika_pom == 1:
                self.slika_pom = 0
            else:
                self.slika_pom = 1

        if (self.brojac % self.broj) == 0:
            if self.tt <= 4:
                self.PokrenutiNaPocetku()
            else:
                for i in range(4):
                    self.tryMove1(i)

        if self.opcija == True:
            if self.brojac1 != 200:
                self.brojac1 = self.brojac1 + 1
            else:
                self.brojac1 = 0
                self.opcija = False
                self.broj = self.broj - 5

        self.brojac = self.brojac + 1
        self.checkPoints()
        super(Board, self).timerEvent(event)

    def checkPoints(self):

        text1 = "Poeni: " + (str(self.player1.poeni)) + " Zivot: " + (str(self.player1.zivot))
        self.label1.setText(text1)
        self.label1.setFont(QtGui.QFont('SansSerif', 15))

        text2 = "Poeni: " + (str(self.player2.poeni)) + " Zivot: " + (str(self.player2.zivot))
        self.label2.setText(text2)
        self.label2.setFont(QtGui.QFont('SansSerif', 15))

    def checkGameOver(self):

        if self.player1.game_over == True and self.player2.game_over == True:

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("PACMAN")

            if self.player1.poeni > self.player2.poeni:
                msgBox.setText('GAME OVER!!! \n Winner is: \n PLAYER 1! \n Points: ' + str(self.player1.poeni))
            elif self.player1.poeni < self.player2.poeni:
                msgBox.setText('GAME OVER!!! \n Winner is: \n PLAYER 2! \n Points: ' + str(self.player2.poeni))
            else:
                msgBox.setText('GAME OVER!!! \n EQUAL RESULT!')

            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()

            if returnValue == QMessageBox.Ok:
                self.parent().close()

    def keyPressEvent(self, event):

        key = event.key()
        t = QTransform()
        t.rotate(90)



        if key == Qt.Key_Left:
            if self.player1.oldkey != 1 and self.tiles[(self.player1.x-1)*22+self.player1.y] != 10:
                self.player1.key = 1

        elif key == Qt.Key_Right:
            if self.player1.x+1 != 21:
                if self.player1.oldkey != 2 and self.tiles[(self.player1.x+1)*22+self.player1.y] != 10:
                    self.player1.key = 2
            else:
                if self.player1.oldkey != 2:
                    self.player1.key = 2


        elif key == Qt.Key_Down: #potrebno je zabraniti ulazak u tunel za duhove
            if self.player1.oldkey != 3 and self.tiles[self.player1.x*22+1+self.player1.y] != 10 and  (self.player1.x != 10 and self.player1.y != 9) :
                self.player1.key = 3

        elif key == Qt.Key_Up:
            if self.player1.oldkey != 4 and self.tiles[self.player1.x*22-1+self.player1.y] != 10:
                self.player1.key = 4
        elif key == Qt.Key_A:
            if self.player2.oldkey != 1 and self.tiles[(self.player2.x-1)*22+self.player2.y] != 10:
                self.player2.key = 1
        elif key == Qt.Key_D:
            if self.player2.x+1 != 21:
                if self.player2.oldkey != 2 and self.tiles[(self.player2.x + 1) * 22 + self.player2.y] != 10:
                    self.player2.key = 2
            else:
                if self.player2.oldkey != 2:
                    self.player2.key = 2

        elif key == Qt.Key_S:
            if self.player2.oldkey != 3 and self.tiles[self.player2.x * 22 + 1 + self.player2.y] != 10 and (self.player2.x != 10 and self.player2.y != 9) :
                self.player2.key = 3
        elif key == Qt.Key_W:
            if self.player2.oldkey != 4 and self.tiles[self.player2.x * 22 - 1 + self.player2.y] != 10:
                self.player2.key = 4
        elif key == Qt.Key_P:
            if self.pauza == False:
                self.timer.stop()
                self.pauza = True
            else:
                self.pauza = False
                self.timer.start(self.timer_interval, self)
        elif key == Qt.Key_Escape:
            self.parent().close()
        else:
            super(Board, self).keyPressEvent(event)

    def tryMove(self, newX, newY,player=p.Player):

        if p.movePlayer(newX, newY, player, self.dots, self.tiles,self):
            self.update()

    def tryMove1(self, z):

        if z == 0:
            g.move(self.tiles, self.ghost1, self.player1, self.player2,self.opcija)
        elif z == 1:
            g.move(self.tiles, self.ghost2, self.player1, self.player2,self.opcija)
        elif z == 2:
            g.move(self.tiles, self.ghost3, self.player1, self.player2,self.opcija)
        else:
            g.move(self.tiles, self.ghost4, self.player1, self.player2,self.opcija)

        if self.player1.pocetak == 1:
            self.player1.key = 5
            self.player1.oldkey = 5
            self.player1.pocetak = 0
        if self.player2.pocetak == 1:
            self.player2.key = 5
            self.player2.oldkey = 5
            self.player2.pocetak = 0
        self.update()

    def PokrenutiNaPocetku(self):

        if self.tt == 0:
            self.ghost1.x = self.ghost1.x + 1
            self.ghost2.x = self.ghost2.x + 1

        elif self.tt == 1:
            self.ghost1.x = self.ghost1.x + 1
            self.ghost2.y = self.ghost2.y - 1
            self.ghost2.way = 1

        elif self.tt == 2:
            g.move(self.tiles, self.ghost2, self.player1,self.player2,self.opcija)
            self.ghost1.y = self.ghost1.y - 1
            self.ghost1.way = 1
            self.ghost3.x = self.ghost3.x - 1
            self.ghost3.way = 1
            self.ghost4.x = self.ghost4.x - 1
            self.ghost4.way = 1

        elif self.tt == 3:
            g.move(self.tiles,self.ghost1,self.player1,self.player2,self.opcija)
            g.move(self.tiles,self.ghost2,self.player1,self.player2,self.opcija)
            self.ghost3.y = self.ghost3.y - 1
            self.ghost4.x = self.ghost4.x - 1

        elif self.tt == 4:
            g.move(self.tiles, self.ghost1, self.player1, self.player2,self.opcija)
            g.move(self.tiles, self.ghost2, self.player1, self.player2,self.opcija)
            g.move(self.tiles, self.ghost3, self.player1, self.player2,self.opcija)
            self.ghost4.y = self.ghost4.y - 1

        self.tt = self.tt + 1
        self.update()

    def levelUp(self):

        promijenjiva = False

        zivot1 = 0
        zivot2 = 0
        bodovi1 = 0
        bodovi2 = 0

        if self.ghost1.sakriven == True and self.ghost2.sakriven == True and self.ghost3.sakriven == True and self.ghost4.sakriven == True:
            promijenjiva = True

        if promijenjiva == True:

            self.level = self.level + 1
            text3 = "Level: " + (str(self.level))
            self.label3.setText(text3)
            self.label3.setFont(QtGui.QFont('SansSerif', 15))

            mapa = self.dots.tacka_pom.copy()
            self.dots.tacka = mapa
            self.tt = 0

            self.ghost1 = g.Ghost(8, 10)
            self.ghost2 = g.Ghost(9, 10)
            self.ghost3 = g.Ghost(11, 10)
            self.ghost4 = g.Ghost(12, 10)

            zivot1 = self.player1.zivot
            zivot2 = self.player2.zivot
            bodovi1 = self.player1.poeni
            bodovi2 = self.player2.poeni

            self.player1 = p.Player()
            self.player1.id = 1
            self.player1.zivot = zivot1
            self.player1.poeni = bodovi1
            self.player2 = p.Player(20, 10)
            self.player2.id = 2
            self.player2.zivot = zivot2
            self.player2.poeni = bodovi2
            self.player2.i = self.player2.i3

            self.opcija = False  #bonuuus
            if self.broj - 2 > 0:
                self.broj = self.broj - 2
            self.brojac = 0
            self.brojac1 = 1

