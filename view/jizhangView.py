from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout, QGridLayout, QStyle, QTableWidget, QHeaderView
from qfluentwidgets import LineEdit, isDarkTheme, EditableComboBox, ComboBox
from common.style_sheet import StyleSheet
from common.add_widget import AddWidget


class jizhangWidget(AddWidget):

    def __init__(self, text: str, parent=None):
        super().__init__(text, parent=parent)
        self.gridLayout = QGridLayout(self)
        # 金额输入框
        self.label = QLabel('金额', self)
        self.LineEdit = LineEdit()
        self.LineEdit.setMaximumWidth(300)
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.addWidget(self.label, 0)
        self.hBoxLayout.addWidget(self.LineEdit, 0)

        # 交易类型选择框
        self.label2 = QLabel('交易类型', self)
        self.comboBox = ComboBox(self)
        self.comboBox.setMinimumWidth(300)
        self.comboBox.addItems(['交通', '饮食', '收入', '衣'])
        self.comboBox.setCurrentIndex(0)
        self.comboBox.currentTextChanged.connect(print)
        self.hBoxLayout2 = QHBoxLayout()
        self.hBoxLayout2.addWidget(self.label2, 0)
        self.hBoxLayout2.addWidget(self.comboBox, 0)

        # 收支选择框
        self.label3 = QLabel('收/支', self)
        self.comboBox2 = ComboBox(self)
        self.comboBox2.setMinimumWidth(300)
        self.comboBox2.addItems(['交通', '饮食', '收入', '衣'])
        self.comboBox2.setCurrentIndex(0)
        self.comboBox2.currentTextChanged.connect(print)
        self.hBoxLayout3 = QHBoxLayout()
        self.hBoxLayout3.addWidget(self.label3, 0)
        self.hBoxLayout3.addWidget(self.comboBox2, 0)

        # 支付方式选择框
        self.label4 = QLabel('支付方式', self)
        self.comboBox3 = ComboBox(self)
        self.comboBox3.setMinimumWidth(300)
        self.comboBox3.addItems(['交通', '饮食', '收入', '衣'])
        self.comboBox3.setCurrentIndex(0)
        self.comboBox3.currentTextChanged.connect(print)
        self.hBoxLayout4 = QHBoxLayout()
        self.hBoxLayout4.addWidget(self.label4, 0)
        self.hBoxLayout4.addWidget(self.comboBox3, 0)

        # 表格展示
        self.table = QTableWidget(5, 5)
        # 设置表格拉伸属性
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.gridLayout.addLayout(self.hBoxLayout, 0, 0)
        self.gridLayout.addLayout(self.hBoxLayout2, 0, 1)
        self.gridLayout.addLayout(self.hBoxLayout3, 1, 0)
        self.gridLayout.addLayout(self.hBoxLayout4, 1, 1)
        self.gridLayout.addWidget(self.table, 2, 0, 1, 2)

        # leave some space for title bar
        self.gridLayout.setContentsMargins(32, 32, 32, 0)  # 此方法可以控制窗体位置
        StyleSheet.JIZHANG_VIEW.apply(self)
