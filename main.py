import biblioteke as bi
import mapa as m
import player as p

if __name__ == '__main__':
    app = bi.QApplication([])
    window = m.Window()
    player = p.Player()
    bi.sys.exit(app.exec_())