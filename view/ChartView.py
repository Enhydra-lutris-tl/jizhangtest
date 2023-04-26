from PySide6.QtCharts import QChartView, QValueAxis, QBarCategoryAxis, QChart, QBarSeries, QBarSet, QLineSeries, \
    QScatterSeries, QPieSeries
from PySide6.QtCore import Qt, QPointF
from PySide6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout
from PySide6.QtGui import QPainter, QPen
from qfluentwidgets import LineEdit, isDarkTheme, EditableComboBox, ComboBox, PushButton, DoubleSpinBox
from common.add_widget import AddWidget
from common.style_sheet import StyleSheet
from main import getIES

class ChartWidget(AddWidget):
    # todo：完善图表内容
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent=parent)
        self.vlot = QVBoxLayout(self)
        self.hlot = QHBoxLayout()
        self.vlot.setContentsMargins(32, 80, 32, 32)
        self.chart_view = QChartView()
        # self.chart_view.setStyleSheet(
        #     'QChartView{'
        #     'background:red'
        #     '}'
        # )
        self.chart = QChart()  # 创建 Chart
        self.chart.setTitle("收/支情况")
        # self.chart.setBackgroundVisible(False)
        self.chart.legend().setVisible(False)
        self.chart.setTheme(QChart.ChartThemeDark)
        self.chart_view.setChart(self.chart)

        # 设置x轴
        # self.axisX = QValueAxis()
        # self.axisX.setRange(200, 500)  # 设置坐标轴范围
        # self.axisX.setLabelFormat("%d")  # 标签格式
        # self.axisX.setTickCount(5)  # 主分隔个数
        # # axisX.setMinorTickCount(4)
        # self.axisX.setTitleText("日期")  # 标题
        # # axisX.setGridLineVisible(True)
        # self.axisX.setMinorGridLineVisible(True)
        # 设置Y轴
        # self.axisY = QValueAxis()
        # self.axisY.setRange(50, 200)
        # self.axisY.setLabelFormat("%d")  # 标签格式
        # self.axisY.setTickCount(4)
        # # axisY.setMinorTickCount(4)
        # self.axisY.setTitleText("金额")
        # # axisY.setGridLineVisible(True)
        # self.axisY.setMinorGridLineVisible(True)

        # self.chart.addAxis(self.axisX, Qt.AlignBottom)
        # self.chart.addAxis(self.axisY, Qt.AlignLeft)

        # self.seriesL = QLineSeries()
        self.seriesL = QPieSeries()
        self.seriesL.setName("收/支情况")
        self.chart.addSeries(self.seriesL)

        # 为直线图表序列设置坐标轴
        # self.chart.setAxisX(self.axisX, self.seriesL)
        # self.chart.setAxisY(self.axisY, self.seriesL)

        self.pushButton = PushButton('绘图')
        self.pushButton_2 = PushButton('清除')
        # 按钮信号
        self.pushButton.clicked.connect(self.jisuan)
        self.pushButton_2.clicked.connect(self.qingchu)
        self.hlot.addWidget(self.pushButton)
        self.hlot.addWidget(self.pushButton_2)
        self.vlot.addWidget(self.chart_view)
        self.vlot.addLayout(self.hlot)

        StyleSheet.CHART_VIEW.apply(self)

    def jisuan(self):
        self.seriesL.clear()

        # t = 250
        # for i in range(11):
        #     y = 0.2 * t + 12
        #     self.seriesL.append(t, y)
        #     t += 20

        value = getIES()
        for i in value:
            self.seriesL.append(i['label'], i['value'])
        self.seriesL.setLabelsVisible(True)


    def qingchu(self):
        self.seriesL.clear()
