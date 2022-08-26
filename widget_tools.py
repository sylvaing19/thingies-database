from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QSizePolicy
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QColor


def apply_shadow(widget: QWidget, radius: float, x_offset: float = 0,
                 y_offset: float = 0, opacity: float = 1):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(radius)
    shadow.setColor(QColor(0, 0, 0, round(opacity * 255)))
    shadow.setOffset(QPointF(x_offset, y_offset))
    widget.setGraphicsEffect(shadow)


def apply_font(widget: QWidget, size: int, bold: bool = False,
               italic: bool = False):
    f = widget.font()
    f.setFamily("Century Gothic")
    f.setBold(bold)
    f.setItalic(italic)
    f.setPixelSize(size)
    widget.setFont(f)


def apply_size_policy(widget: QWidget):
    widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
