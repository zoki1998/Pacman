import biblioteke as bi



class



def keyPressEvent(self, event):


key = event.key( )
if key == Qt.Key_Left:
    self.tryMove(self, self.curX - 1, self.curY)

elif key == Qt.Key_Right:
    self.tryMove(self.curPiece, self.curX + 1, self.curY)

elif key == Qt.Key_Down:
    self.tryMove(self.curPiece.rotateRight( ), self.curX, self.curY)

elif key == Qt.Key_Up:
    self.tryMove(self.curPiece.rotateLeft( ), self.curX, self.curY)