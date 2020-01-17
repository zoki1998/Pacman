from threading import Thread
import player as p
import biblioteke as bi


def nekafun(player):

    print(player.y)
    player.y = 555


if __name__ == '__main__':
    pl = p.Player()
    pl.y = 444
    thread = Thread(target=nekafun, args=(pl,))
    thread.start()
    thread.join()
    print("thread finished...exiting")
    print(pl.y)
