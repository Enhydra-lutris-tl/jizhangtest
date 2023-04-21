from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout
from qfluentwidgets import LineEdit, isDarkTheme
from common.style_sheet import StyleSheet
from common.add_widget import AddWidget


class jizhangWidget(AddWidget):

    def __init__(self, text: str, parent=None):
        super().__init__(text, parent=parent)
        self.label = QLabel('记账页面', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.LineEdit = LineEdit()
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.LineEdit)

        # leave some space for title bar
        self.hBoxLayout.setContentsMargins(0, 32, 0, 0)
        StyleSheet.JIZHANG_VIEW.apply(self)
