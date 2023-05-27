from PySide6.QtCharts import QChartView, QValueAxis, QBarCategoryAxis, QChart, QBarSeries, QBarSet, QLineSeries, \
    QScatterSeries, QPieSeries
from PySide6.QtCore import Qt, QPointF
from PySide6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout
from PySide6.QtGui import QPainter, QPen
from qfluentwidgets import LineEdit, isDarkTheme, EditableComboBox, ComboBox, PushButton, DoubleSpinBox
from common.add_widget import AddWidget
from common.style_sheet import StyleSheet
from main import getIES


class RegularlyRemind(AddWidget):
    # todo：完善消息弹窗功能
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.Label = QLabel('1111')
        self.hBoxLayout.addWidget(self.Label)

        StyleSheet.CHART_VIEW.apply(self)


