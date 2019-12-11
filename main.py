import biblioteke as bi
import mapa as m
import player as p
from tkinter import *

if __name__ == '__main__':
    app = bi.QApplication([])
    window = m.Window()
    bi.sys.exit(app.exec_())