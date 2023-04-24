from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout, QGridLayout, QStyle, QTableWidget, QHeaderView, \
    QTableWidgetItem
from qfluentwidgets import LineEdit, isDarkTheme, EditableComboBox, ComboBox,PushButton
from common.style_sheet import StyleSheet
from common.add_widget import AddWidget
from main import ceshi as getValue


class jizhangWidget(AddWidget):
    # todo：完善记账页面内容
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent=parent)
        self.gridLayout = QGridLayout(self)

        # 金额输入框
        self.label = QLabel('金额', self)
        self.LineEdit = LineEdit()
        self.LineEdit.setMinimumWidth(300)
        self.LineEdit.setMaximumWidth(300)
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.addWidget(self.label, 0)
        self.hBoxLayout.addWidget(self.LineEdit, 0)

        # 交易类型选择框
        self.label2 = QLabel('交易类型', self)
        self.comboBox = ComboBox(self)
        self.comboBox.setMinimumWidth(300)
        self.comboBox.setMaximumWidth(300)
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
        self.comboBox2.setMaximumWidth(300)
        self.comboBox2.addItems(['收入', '支出'])
        self.comboBox2.setCurrentIndex(0)
        self.comboBox2.currentTextChanged.connect(print)
        self.hBoxLayout3 = QHBoxLayout()
        self.hBoxLayout3.addWidget(self.label3, 0)
        self.hBoxLayout3.addWidget(self.comboBox2, 0)

        # 支付方式选择框
        self.label4 = QLabel('支付方式', self)
        self.comboBox3 = ComboBox(self)
        self.comboBox3.setMinimumWidth(300)
        self.comboBox3.setMaximumWidth(300)
        self.comboBox3.addItems(['支付宝', '微信', '银行卡', '花呗'])
        self.comboBox3.setCurrentIndex(0)
        self.comboBox3.currentTextChanged.connect(print)
        self.hBoxLayout4 = QHBoxLayout()
        self.hBoxLayout4.addWidget(self.label4, 0)
        self.hBoxLayout4.addWidget(self.comboBox3, 0)

        # 提交按钮
        self.subMitButton = PushButton('提交')
        self.rsMitButton = PushButton('重置')
        self.hBoxLayout5 = QHBoxLayout()
        self.hBoxLayout5.addWidget(self.rsMitButton, 0)
        self.hBoxLayout5.addWidget(self.subMitButton, 0)

        # 表格展示
        mainValue = getValue()
        cloumsCount = mainValue.shape[0]
        rowsCount = mainValue.shape[1]
        headerItemText = mainValue.columns.values
        self.table = QTableWidget(cloumsCount, 5)
        self.table.setHorizontalHeaderLabels(headerItemText)
        for i in range(cloumsCount):
            for b in range(rowsCount):
                self.table.setItem(i, b, QTableWidgetItem(str(mainValue[headerItemText[b]][i])))
        # 设置表格拉伸属性
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.gridLayout.addLayout(self.hBoxLayout, 0, 1)
        self.gridLayout.addLayout(self.hBoxLayout2, 0, 2)
        self.gridLayout.addLayout(self.hBoxLayout3, 1, 1)
        self.gridLayout.addLayout(self.hBoxLayout4, 1, 2)
        self.gridLayout.addWidget(self.table, 3, 0, 1, 3)
        self.gridLayout.addLayout(self.hBoxLayout5, 2, 2)
        # leave some space for title bar
        self.hBoxLayout.setContentsMargins(15, 15, 15, 15)
        self.hBoxLayout2.setContentsMargins(15, 15, 0, 15)
        self.hBoxLayout3.setContentsMargins(15, 15, 15, 15)
        self.hBoxLayout4.setContentsMargins(15, 15, 0, 15)
        self.gridLayout.setContentsMargins(32, 32, 32, 32)  # 此方法可以控制窗体位置
        StyleSheet.JIZHANG_VIEW.apply(self)
