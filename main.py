import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QHBoxLayout,
                             QTabWidget, QMessageBox, QPushButton, QVBoxLayout,
                             QFrame, QGraphicsDropShadowEffect, QSizePolicy)
from PyQt5.QtCore import QObject, QEvent, Qt
from PyQt5.QtGui import QColor


def apply_shadow(widget: QWidget, radius: float):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(radius)
    shadow.setColor(Qt.black)
    shadow.setOffset(0, 0)
    widget.setGraphicsEffect(shadow)


def apply_font(widget: QWidget, size: int, bold: bool = False,
               italic: bool = False):
    f = widget.font()
    f.setFamily("Century Gothic")
    f.setBold(bold)
    f.setItalic(italic)
    f.setPixelSize(size)
    widget.setFont(f)


class Toolbar(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet("background-color: #008396")
        self.setFixedHeight(120)
        apply_shadow(self, 100)
        grid = QHBoxLayout()
        grid.setContentsMargins(12, 12, 12, 12)
        grid.setSpacing(12)

        self._b_back = QPushButton("Back", self)
        self._b_back.setFixedWidth(216)
        self._b_back.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        apply_font(self._b_back, 72)
        self._b_back.setStyleSheet(
            "background-color: #2F4858; color: white; border: none;")
        apply_shadow(self._b_back, 10)
        grid.addWidget(self._b_back)
        grid.addStretch(1)
        self.setLayout(grid)


class MainWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        grid = QVBoxLayout()
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(0)
        f = QFrame(self)
        grid.addWidget(Toolbar(self))
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
