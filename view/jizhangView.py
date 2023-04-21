from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout
from qfluentwidgets import LineEdit, isDarkTheme
from common.style_sheet import StyleSheet


class jizhangWidget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(' ', '-'))
        self.label = QLabel(text, self)
        self.label.setObjectName('ceshi')
        self.label.setAlignment(Qt.AlignCenter)
        self.LineEdit = LineEdit()
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.LineEdit)

        # leave some space for title bar
        self.hBoxLayout.setContentsMargins(0, 32, 0, 0)
        StyleSheet.JIZHANG_VIEW.apply(self)
