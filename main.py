import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QHBoxLayout,
                             QTabWidget, QMessageBox, QPushButton)
from PyQt5.QtCore import QObject, QEvent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


def except_hook(t, value, traceback):
    sys.__excepthook__(t, value, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win.resize(1920, 1080)
    ret = app.exec()
    sys.exit(ret)
