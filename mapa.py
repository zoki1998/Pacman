from PyQt5 import QtGui
from PyQt5.QtWidgets import QGraphicsScene,QLabel

from PyQt5.QtGui import QTransform, QImage
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
import sys, time
import dots as dot

import player as p
import ghost as g


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.tboard = Board(self)
        self.statusbar = self.statusBar()

        self.initUI( )

    def initUI(self):
        self.setWindowTitle('Pacman')
        self.setCentralWidget(self.tboard)
        self.setWindowIcon(QtGui.QIcon('pacman.ico'))
        self.resize(882, 954)

        self.tboard.timer.start(self.tboard.timer_interval, self.tboard)


        self.center()
        self.show()

    def center(self):
        """centers the window on the screen"""

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2-40)


class Board(QFrame):
    BoardWidth = 882
    BoardHeight = 924

    def __init__(self, parent):
        msg2Statusbar = pyqtSignal(str)

        self.pp = p.Player()
        self.ghost1 = g.Ghost(8,10)
        self.ghost2 = g.Ghost(9,10)
        self.ghost3 = g.Ghost(11,10)
        self.ghost4 = g.Ghost(12,10)
        self.tt=0;
        self.broj = 0
        super().__init__(parent)
        self.resize(882, 924)
        self.shape = 10
        self.dots = dot.Tacke()
        self.s1 = 1 # za mijenjanje slike
        text = "Poeni: 0    Zivot : 3"
        self.lbl3 = QLabel(text,self)
        self.lbl3.setFont(QtGui.QFont('SansSerif', 30))
        self.brojac=0
        self.lbl3.move(10, 930)
        self.key = 0
        self.keyold = 0
        self.setFocusPolicy(Qt.StrongFocus)

        self.color1 = 0xFF0000
        self.color2 = 0x000000
        self.timer_interval = 50
        self.scene = QGraphicsScene()
        self.scene.addItem(self.pp)

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
        rect = self.contentsRect( )
        for x in range(21):
            for y in range(22):
                self.setshape(self.tiles[x * 22 + y])
                self.draw(x * 42, y * 42, painter, QColor(0x000000))
                self.dots.paint(painter, x, y)

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

        #  painter.setPen(color.darker())
        #desna

        if self.shape == 1 or self.shape == 4 or self.shape == 5 or self.shape == 8 or self.shape == 13 or self.shape == 14:
            painter.drawLine(x + 1, y + self.squareWidth(),
                         x + self.squareHeight()+1, y + self.squareWidth())
        #donja
        if self.shape == 2 or self.shape == 4 or self.shape == 7 or self.shape == 12 or self.shape == 13:
            painter.drawLine(x + self.squareHeight()+1,
                         y + self.squareWidth(), x + self.squareHeight(), y)
        self.pp.paint(painter)
        self.ghost1.paint(painter)
        self.ghost2.paint(painter)
        self.ghost3.paint(painter)
        self.ghost4.paint(painter)


    def squareWidth(self):
        return 42

    def squareHeight(self):
        return 42

    def timerEvent(self, event):
        t = QTransform()
        if(self.brojac%10) == 0:
            if self.key != 0:
                if self.key == 1:
                    if self.s1 == 1:
                        self.pp.i = self.pp.i3
                        self.s1 = 0
                    else:
                        self.pp.i = self.pp.img2
                        self.s1 = 1
                    self.tryMove(self.pp.x - 1, self.pp.y)

                elif self.key == 2:
                    if self.s1 == 1:
                        self.pp.i = self.pp.i2
                        self.s1 = 0
                    else:
                        self.pp.i = self.pp.img
                        self.s1 = 1

                    self.tryMove(self.pp.x + 1, self.pp.y)
                elif self.key == 3:
                    self.pp.i = self.pp.i2
                    self.pp.i.convertToFormat(QImage.Format_RGB888)
                    t.rotate(90)

                    if self.s1 == 1:
                        self.pp.i = self.pp.i.transformed(t)
                        self.s1 = 0
                    else:
                        self.pp.i = self.pp.img.transformed(t)
                        self.s1 = 1

                    self.tryMove(self.pp.x, self.pp.y + 1)
                elif self.key == 4:
                    self.pp.i = self.pp.i2
                    self.pp.i.convertToFormat(QImage.Format_RGB888)
                    t.rotate(-90)
                    if self.s1 == 1:
                        self.pp.i = self.pp.i.transformed(t)
                        self.s1 = 0
                    else:
                        self.pp.i = self.pp.img.transformed(t)
                        self.s1 = 1
                    self.tryMove(self.pp.x, self.pp.y - 1)
        if (self.brojac % (10 - self.broj)) == 0:
            if self.tt<=4:
                self.PokrenutiNaPocetku()
            else:
                for i in range(4):
                    self.tryMove1(i)
        text = "Poeni: "+(str(self.pp.poeni))+" Zivot: "+(str(self.pp.zivot))
        self.lbl3.setText(text)
        self.lbl3.setFont(QtGui.QFont('SansSerif', 30))
        self.brojac=self.brojac+1
        super(Board, self).timerEvent(event)

    def keyPressEvent(self, event):

        key = event.key()
        t = QTransform()
        t.rotate(90)

        if key == Qt.Key_P:
            self.pause()
            return

        elif key == Qt.Key_Left:
            if self.keyold != 1 and self.tiles[(self.pp.x-1)*22+self.pp.y] != 10:
                self.key = 1

        elif key == Qt.Key_Right:
            if self.keyold != 2 and self.tiles[(self.pp.x+1)*22+self.pp.y] != 10:
                self.key = 2

        elif key == Qt.Key_Down:
            if self.keyold != 3 and self.tiles[self.pp.x*22+1+self.pp.y] != 10:
                self.key = 3

        elif key == Qt.Key_Up:
            if self.keyold != 4 and self.tiles[self.pp.x*22-1+self.pp.y] != 10:
                self.key = 4
        else:
            super(Board, self).keyPressEvent(event)

    def tryMove(self, newX, newY):

        x = newX
        y = newY
        if x < 0 or x*42 >= Board.BoardWidth or y < 0 or y*42 >= Board.BoardHeight:
            if x == -1 and y == 10 and self.key == 1:
                x = 20
                y = 10
                self.keyold = self.key
                self.pp.x = x
                self.pp.y = y
                if self.dots.tacka_pom[x*22 + y] != 0:
                    if self.dots.tacka_pom[x * 22 + y] == 1:
                        self.pp.poeni = self.pp.poeni + 1
                    else:
                        self.pp.poeni = self.pp.poeni + 2
                    #self.dots.tacka_pom[x*22 + y] = 0
                    self.dots.tacka[x*22 + y] = 0
                self.update()
                return True
            elif x == 21 and y == 10 and self.key == 2:
                x = 0
                y = 10
                self.keyold = self.key
                self.pp.x = x
                self.pp.y = y
                if self.dots.tacka_pom[x*22 + y] != 0:
                    if self.dots.tacka_pom[x * 22 + y] == 1:
                        self.pp.poeni = self.pp.poeni + 1
                    else:
                        self.pp.poeni = self.pp.poeni + 2
                    #self.dots.tacka_pom[x*22 + y] = 0

                    self.dots.tacka[x*22 + y] = 0
                self.update()
                return True
            else:
                 self.key = 0
                 return False
        if self.tiles[x * 22 + y] == 10:
            self.key = self.keyold
            return False

        self.keyold = self.key
        self.pp.x = x
        self.pp.y = y
        if self.dots.tacka_pom[x*22 + y] != 0:
            if self.dots.tacka_pom[x * 22 + y] == 1:
                self.pp.poeni = self.pp.poeni + 1
            else:
                self.pp.poeni = self.pp.poeni + 2
            # self.dots.tacka_pom[x*22 + y] = 0
            self.dots.tacka[x * 22 + y] = 0

        self.update()

        return True

    def tryMove1(self, z):

        if z == 0:
            g.move(self.tiles, self.ghost1, self.pp)
        elif z == 1:
            g.move(self.tiles, self.ghost2, self.pp)
        elif z == 2:
            g.move(self.tiles, self.ghost3, self.pp)
        else:
            g.move(self.tiles, self.ghost4, self.pp)
        if self.pp.pocetak == 1:
            self.key = 5
            self.keyold = 5
            self.pp.pocetak = 0
        self.update()

    def PokrenutiNaPocetku(self):
        if self.tt == 0:
            self.ghost1.x=self.ghost1.x+1
            self.ghost2.x=self.ghost2.x+1
        elif self.tt== 1:
            self.ghost1.x = self.ghost1.x + 1
            self.ghost2.y = self.ghost2.y - 1
            self.ghost2.way=1
        elif self.tt==2:

            g.move(self.tiles, self.ghost2, self.pp)
            self.ghost1.y=self.ghost1.y - 1
            self.ghost1.way = 1
            self.ghost3.x=self.ghost3.x-1
            self.ghost3.way=1
            self.ghost4.x=self.ghost4.x-1
            self.ghost4.way=1
        elif self.tt==3:
            g.move(self.tiles,self.ghost1,self.pp)
            g.move(self.tiles,self.ghost2,self.pp)
            self.ghost3.y = self.ghost3.y - 1
            self.ghost4.x = self.ghost4.x - 1
        elif self.tt==4:
            g.move(self.tiles, self.ghost1, self.pp)
            g.move(self.tiles, self.ghost2, self.pp)
            g.move(self.tiles, self.ghost3, self.pp)
            self.ghost4.y = self.ghost4.y - 1

        self.tt=self.tt+1
        self.update()















