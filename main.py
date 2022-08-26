import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QHBoxLayout,
                             QTabWidget, QMessageBox, QPushButton, QVBoxLayout,
                             QFrame, QGraphicsDropShadowEffect, QSizePolicy)
from PyQt5.QtCore import QObject, QEvent, Qt
from PyQt5.QtGui import QColor
from title_bar import TitleBar


class MainWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        grid = QVBoxLayout()
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(0)
        f = QFrame(self)
        grid.addWidget(TitleBar(self))
        f.setStyleSheet("background-color: #2F4858")
        grid.addWidget(f)
        self.setLayout(grid)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        w = MainWidget(self)
        self.setCentralWidget(w)


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
