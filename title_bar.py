from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QHBoxLayout,
                             QTabWidget, QMessageBox, QPushButton, QVBoxLayout,
                             QFrame, QGraphicsDropShadowEffect, QLabel)
from PyQt5.QtCore import QObject, QEvent, Qt, QPointF
from PyQt5.QtGui import QColor, QPixmap
from widget_tools import apply_shadow, apply_font, apply_size_policy

# Colors
# Light
# #24E3B9
# #00C3B6
# #00A3AA
# #008396
# #276579
# #2F4858
# Dark

TITLE_BAR_STYLESHEET = """
QFrame {
    background-color: #008396;
}

QPushButton {
    background-color: #2F4858;
    color: white;
    border: none;
}

QPushButton:hover {
    background-color: #276579;
}

QPushButton:pressed {
    background-color: #00A3AA;
}

QLabel {
    background: none;
    color: white;
    border: none;
}
"""


class TitleBar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Self styling
        self.setStyleSheet(TITLE_BAR_STYLESHEET)
        self.setFixedHeight(120)
        apply_shadow(self, 100)

        # Button "Back"
        self._b_back = QPushButton("Back", self)
        self._b_back.setFixedWidth(216)
        apply_shadow(self._b_back, 12, 4, 4, 0.9)
        apply_font(self._b_back, 72)
        apply_size_policy(self._b_back)

        # Icon
        self._icon = QLabel(self)
        self._icon.setFixedWidth(156)
        apply_size_policy(self._icon)
        self._icon.setPixmap(QPixmap("icon.png").scaled(
            156, 96, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        # Title
        self._title = QLabel("Resistors", self)
        self._title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        apply_font(self._title, 72)
        apply_size_policy(self._title)

        # Info
        self._info = QLabel("698", self)
        self._info.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        apply_font(self._info, 72)
        apply_size_policy(self._info)

        # Sub-info
        self._sub_info = QLabel("items found", self)
        self._sub_info.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        apply_font(self._sub_info, 45)
        apply_size_policy(self._sub_info)

        # Button "List"
        self._b_list = QPushButton("List", self)
        self._b_list.setFixedWidth(216)
        apply_shadow(self._b_list, 12, 4, 4, 0.9)
        apply_font(self._b_list, 72)
        apply_size_policy(self._b_list)

        # Content layout
        grid = QHBoxLayout()
        grid.setContentsMargins(12, 12, 12, 12)
        grid.setSpacing(12)
        grid.addWidget(self._b_back)
        grid.addWidget(self._icon)
        grid.addWidget(self._title, stretch=1)
        grid.addWidget(self._info, stretch=1)
        sub_info_grid = QVBoxLayout()
        sub_info_grid.addSpacing(23)
        sub_info_grid.addWidget(self._sub_info)
        grid.addLayout(sub_info_grid)
        grid.addWidget(self._b_list)
        self.setLayout(grid)
