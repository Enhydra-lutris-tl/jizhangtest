from PySide6.QtWidgets import QFrame
from common.style_sheet import StyleSheet


class AddWidget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(' ', '-'))
