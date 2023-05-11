import json
import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout, QGridLayout, QStyle, QTableWidget, QHeaderView, \
    QTableWidgetItem, QTableView, QFileDialog
from qfluentwidgets import ComboBox, PushButton, DoubleSpinBox, TableView, TableItemDelegate, TableWidget
from common.style_sheet import StyleSheet
from common.add_widget import AddWidget
from main import ceshi as getValue
from datetime import datetime
# import ruamel.yaml as yaml


class jizhangWidget(AddWidget):
    # todo：完善记账页面内容
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent=parent)
        self.gridLayout = QGridLayout(self)

        # 金额输入框
        self.label = QLabel('金额', self)
        self.DoubleSpinBox = DoubleSpinBox()
        self.DoubleSpinBox.setMinimumWidth(300)
        self.DoubleSpinBox.setMaximumWidth(300)
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.addWidget(self.label, 0)
        self.hBoxLayout.addWidget(self.DoubleSpinBox, 0)

        # 交易类型选择框
        self.label2 = QLabel('交易分类', self)
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
        self.label4 = QLabel('收/付款方式', self)
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
        self.subMitButton = PushButton('添加')
        self.subMitButton.clicked.connect(self.addTableValue)
        self.rsMitButton = PushButton('重置')
        self.rsMitButton.clicked.connect(self.Reset)
        self.hBoxLayout5 = QHBoxLayout()
        self.hBoxLayout5.addWidget(self.rsMitButton, 0)
        self.hBoxLayout5.addWidget(self.subMitButton, 0)

        # 导入按钮
        self.importButton = PushButton('导入')
        self.importButton.setMaximumWidth(50)
        # self.importButton.clicked.connect(self.select_folder)

        # 操作情况反馈标签
        self.feedbackLabel = QLabel('此位置展示操作反馈')
        self.feedbackLabel.adjustSize()  # 自适应宽度
        self.feedbackLabel.setWordWrap(True)  # 自动换行
        self.feedbackLabel.setObjectName('feedbackText')  # 独立样式

        # 表格展示
        mainValue = getValue()
        LinesCount = mainValue.shape[0]
        rowsCount = mainValue.shape[1]
        headerItemText = mainValue.columns.values
        self.table = TableView()

        # 模型层
        self.model = QStandardItemModel(LinesCount, 5)
        self.model.setHorizontalHeaderLabels(headerItemText)
        for i in range(LinesCount):
            for b in range(rowsCount):
                self.model.setItem(i, b, QStandardItem(str(mainValue[headerItemText[b]][i])))

        # 视图层绑定模型层
        self.table.setModel(self.model)

        # 设置表格拉伸属性
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().hide()

        # 设置单元格无法编辑
        self.table.setEditTriggers(QTableView.NoEditTriggers)

        # 布局
        self.gridLayout.addLayout(self.hBoxLayout, 0, 1)
        self.gridLayout.addLayout(self.hBoxLayout2, 0, 2)
        self.gridLayout.addLayout(self.hBoxLayout3, 1, 1)
        self.gridLayout.addLayout(self.hBoxLayout4, 1, 2)
        self.gridLayout.addWidget(self.table, 3, 0, 1, 3)
        self.gridLayout.addLayout(self.hBoxLayout5, 2, 2)
        self.gridLayout.addWidget(self.importButton, 2, 0)
        self.gridLayout.addWidget(self.feedbackLabel, 2, 1)

        # 为标题栏留出一些空间
        self.hBoxLayout.setContentsMargins(15, 15, 15, 15)
        self.hBoxLayout2.setContentsMargins(15, 15, 0, 15)
        self.hBoxLayout3.setContentsMargins(15, 15, 15, 15)
        self.hBoxLayout4.setContentsMargins(15, 15, 0, 15)
        self.gridLayout.setContentsMargins(32, 32, 32, 32)  # 此方法可以控制窗体位置
        StyleSheet.JIZHANG_VIEW.apply(self)

    # 重置按钮功能
    def Reset(self):
        self.comboBox.setCurrentIndex(0)
        self.comboBox2.setCurrentIndex(0)
        self.comboBox3.setCurrentIndex(0)
        self.DoubleSpinBox.setValue(0.00)

    # 添加按钮功能 并添加到数据库
    def addTableValue(self):
        DoubleSpinBoxText = self.DoubleSpinBox.text()
        comboxText = self.comboBox.text()
        combox2Text = self.comboBox2.text()
        combox3Text = self.comboBox3.text()
        nowDateTime = datetime.now().strftime("%Y-%m-%d %H:%M")
        if DoubleSpinBoxText == '0.00':
            print('内容为空，请输入正确金额')
            self.feedbackLabel.setText('内容为空，请输入正确金额')
        else:
            newValue = json.dumps({
                "nowDate": nowDateTime,
                "trade": comboxText,
                "iae": combox2Text,
                "payMethod": combox3Text,
                "moneyValue": DoubleSpinBoxText
            }, ensure_ascii=False)
            print(newValue)
            self.feedbackLabel.setText(newValue)

    # def select_folder(self):
    #     test_file = os.path.abspath('.')
    #     folder_file = QFileDialog.getExistingDirectory(self, '选择文件夹')
    #     print(folder_file, test_file)
    #
    #     """
    #     自动生成yaml文件
    #     """
    #     data = {
    #         "folder_file": folder_file,
    #     }
    #     with open(test_file + "/config.yaml", "w") as f:  # 写文件
    #         yaml.safe_dump(data=data, stream=f)
